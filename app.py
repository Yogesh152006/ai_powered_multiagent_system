from flask import Flask, render_template
from scraper import scrape_news
from cleaner import clean_data
from extractor import extract_information
from predictor import predict_growth
from insights import generate_insight

app = Flask(__name__)

@app.route("/")

def home():

    df = scrape_news()

    df = clean_data(df)

    startups = []

    for _, row in df.iterrows():

        info = extract_information(row["title"])

        stage = predict_growth(row["title"])

        insight = generate_insight(info)

        startups.append({

            "title": row["title"],

            "info": info,

            "stage": stage,

            "insight": insight

        })

    return render_template(
        "index.html",
        startups=startups
    )

if __name__ == "__main__":
    app.run(debug=True)