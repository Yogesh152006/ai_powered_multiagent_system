# 🚀 AI-Powered Multi-Agent Startup Intelligence System

An AI-powered platform that automatically collects startup news from the web, extracts important business insights, predicts startup growth stages, and presents the results through a simple Flask-based dashboard.

## 📌 Project Overview

The AI-Powered Multi-Agent Startup Intelligence System automates startup market intelligence by combining web scraping, Natural Language Processing (NLP), Machine Learning, and visualization.

Instead of manually reading startup news articles, the system collects news from multiple sources, processes the content, extracts valuable information, predicts startup growth stages, and generates AI-driven insights.

---

## 🎯 Features

- 🌐 Automated Startup News Scraping
- 🧹 Data Cleaning & Preprocessing
- 🧠 AI-based Information Extraction
- 📈 Startup Growth Stage Prediction
- 💡 Automated Insight Generation
- 📊 Flask Dashboard for Visualization
- 💾 CSV Data Storage
- ⚡ Modular Multi-Agent Architecture

---

## 🏗️ Project Architecture

```
                Startup News Websites
                         │
                         ▼
                Web Scraping Agent
                         │
                         ▼
             Data Cleaning Agent
                         │
                         ▼
         Information Extraction Agent
                         │
                         ▼
        Growth Prediction Agent (ML)
                         │
                         ▼
        Insight Generation Agent
                         │
                         ▼
          startups.csv Dataset
                         │
                         ▼
              Flask Web Dashboard
```

---

## 🛠️ Technologies Used

### Programming Language

- Python 3.x

### Backend

- Flask

### Data Processing

- Pandas
- NumPy

### Web Scraping

- Requests
- BeautifulSoup4

### Machine Learning

- Scikit-learn

### Data Storage

- CSV

### Frontend

- HTML
- CSS
- Jinja2 Templates

---

## 📂 Project Structure

```
AI_Powered_MultiAgent_System/

│
├── app.py
├── scraper.py
├── cleaner.py
├── extractor.py
├── predictor.py
├── insights.py
├── startups.csv
├── requirements.txt
│
├── templates/
│      └── index.html
│
├── static/
│      └── style.css
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Yogesh152006/ai_powered_multiagent_system.git
```

Move into the project

```bash
cd ai_powered_multiagent_system
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📊 Workflow

1. Scrape startup news articles
2. Clean and preprocess the collected data
3. Extract startup information using NLP
4. Predict startup growth stage
5. Generate AI insights
6. Store structured data in `startups.csv`
7. Display results on the Flask dashboard

---

## 🤖 Multi-Agent Components

### 1. Web Scraping Agent

Collects startup-related news from online sources.

### 2. Data Cleaning Agent

Removes duplicate records and cleans extracted text.

### 3. Information Extraction Agent

Extracts:

- Startup Name
- Industry
- Funding
- Investors
- Location
- Technologies

### 4. Growth Prediction Agent

Predicts startup growth stage using machine learning.

Possible stages include:

- Seed Stage
- Early Stage
- Growth Stage
- Scale-Up

### 5. Insight Generation Agent

Generates meaningful business insights based on extracted information.

Example:

> "The startup is attracting significant investor attention and is likely to experience rapid growth."

---

## 📈 Output

The dashboard displays:

- Startup Headline
- Growth Stage
- AI Generated Insights

The structured data is also stored in:

```
startups.csv
```

---

## 📦 Python Libraries

- Flask
- Requests
- BeautifulSoup4
- Pandas
- NumPy
- Scikit-learn

---

## 🚀 Future Enhancements

- Multi-source news aggregation
- Real-time news streaming
- Transformer-based NLP models
- Sentiment Analysis
- Startup Funding Prediction
- Investor Recommendation System
- Interactive Charts
- MySQL Database Integration
- REST API Support
- Docker Deployment

---

## 🎓 Learning Outcomes

This project demonstrates practical implementation of:

- Web Scraping
- Natural Language Processing
- Machine Learning
- Data Cleaning
- Data Visualization
- Flask Development
- Multi-Agent AI Systems
- Python Automation

---

## 👨‍💻 Author

**YogeshWaran**

Computer Science Engineering (AI & ML)

GitHub: https://github.com/Yogesh152006

---

## ⭐ If you found this project useful, consider giving it a star!
