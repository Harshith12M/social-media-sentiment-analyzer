from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import plotly
import plotly.graph_objs as go
import json

# Initialize Flask app
app = Flask(__name__)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to classify sentiment
def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    if compound > 0.05:
        return 'Positive'
    elif compound < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Route: Home page
@app.route('/')
def index():
    return render_template('index.html')

# Route: Analyze single post
@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    sentiment = analyze_sentiment(text)
    return render_template('result.html', post={'text': text, 'sentiment': sentiment})

# Route: Analyze CSV upload
@app.route('/analyze_csv', methods=['POST'])
def analyze_csv():
    file = request.files['file']
    df = pd.read_csv(file, header=None, names=['text'])
    posts = []

    for text in df['text']:
        sentiment = analyze_sentiment(text)
        posts.append({'text': text, 'sentiment': sentiment})

    # Count sentiments
    positive = sum(1 for post in posts if post['sentiment'] == 'Positive')
    negative = sum(1 for post in posts if post['sentiment'] == 'Negative')
    neutral = sum(1 for post in posts if post['sentiment'] == 'Neutral')

    # Create Pie chart
    labels = ['Positive', 'Negative', 'Neutral']
    values = [positive, negative, neutral]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker_colors=['#4CAF50', '#F44336', '#FFC107'])])
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('summary.html', posts=posts, graph_json=graph_json)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
