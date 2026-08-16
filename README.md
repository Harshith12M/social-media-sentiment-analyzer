Social Media Sentiment Analyzer

A Python Flask web application that analyzes the sentiment of social media posts and classifies them as Positive, Negative, or Neutral using VADER Sentiment Analysis.

The application supports both single-text analysis and bulk CSV analysis, with an interactive Plotly chart to visualize the overall sentiment distribution.

📌 Project Overview

Social media platforms generate a large amount of text every day. Manually analyzing this content to understand whether users have positive, negative, or neutral opinions can be difficult.

This project provides a simple web-based solution where users can:

Enter a single social media post and analyze its sentiment.
Upload a CSV file containing multiple posts.
Automatically classify each post as Positive, Negative, or Neutral.
View all analyzed posts and their sentiment.
Visualize the overall sentiment distribution using an interactive pie chart.
🚀 Features
1. Single Post Analysis

Users can enter a social media post directly into the web application.

Example:

I love this application! It is amazing.

The application analyzes the text and displays:

Sentiment: Positive
2. CSV File Analysis

Users can upload a CSV file containing multiple posts.

The application:

Reads the CSV using Pandas.
Processes each post.
Performs sentiment analysis using VADER.
Classifies each post.
Displays the results in a table.
Calculates the Positive, Negative, and Neutral counts.
3. Sentiment Visualization

The project uses Plotly to generate an interactive pie chart showing the distribution of:

Positive
Negative
Neutral
4. Web Interface

The frontend is developed using:

HTML
CSS
Jinja2 templates
🛠️ Technologies Used
Technology	Purpose
Python	Main programming language
Flask	Backend web framework
VADER Sentiment	NLP-based sentiment analysis
Pandas	CSV processing and data handling
Plotly	Interactive data visualization
HTML	Frontend structure
CSS	Frontend styling
Jinja2	Dynamic HTML rendering
Git	Version control
GitHub	Source-code repository
Gunicorn	Production WSGI server
🤖 Sentiment Analysis

This project uses VADER (Valence Aware Dictionary and sEntiment Reasoner).

VADER is a lexicon and rule-based sentiment analysis tool that is particularly suitable for short and informal text such as social media posts.

It provides four sentiment scores:

Positive
Negative
Neutral
Compound

The compound score ranges from -1 to +1.

The project classifies the sentiment using the following thresholds:

Compound Score	Classification
Greater than 0.05	Positive
Less than -0.05	Negative
Between -0.05 and 0.05	Neutral

For example:

"I love this app!"
→ Positive
"The service was terrible."
→ Negative
"It's just okay."
→ Neutral/depends on the VADER score
🏗️ Project Architecture
                    User
                     |
                     v
              Flask Web Interface
                     |
          +----------+----------+
          |                     |
          v                     v
    Single Text Input      CSV File Upload
          |                     |
          v                     v
       VADER                  Pandas
          |                     |
          +----------+----------+
                     |
                     v
             Sentiment Result
                     |
          +----------+----------+
          |                     |
          v                     v
     Result Page          Summary Page
                                |
                                v
                         Plotly Pie Chart
📂 Project Structure
social-media-sentiment-analyzer/
│
├── app.py
├── requirements.txt
├── Procfile
├── sample.csv
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── summary.html
│
└── static/
    └── css/
        └── style.css

Installation

Clone the repository:

git clone https://github.com/Harshith12M/social-media-sentiment-analyzer.git
cd social-media-sentiment-analyzer

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open:

http://127.0.0.1:5000
📊 Future Enhancements
Database integration.
User authentication.
Real-time social media data.
Sentiment analysis dashboards.
Advanced ML/NLP models such as BERT or RoBERTa.
👨‍💻 Project Type

Python Full-Stack Web Application

Domain: Natural Language Processing (NLP)

GitHub: https://github.com/Harshith12M/social-media-sentiment-analyzer
