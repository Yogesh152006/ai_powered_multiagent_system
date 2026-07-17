import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_news():

    url = "https://techcrunch.com/category/startups/"

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []

    articles = soup.find_all("h3")

    for article in articles:

        title = article.get_text(strip=True)

        headlines.append({
            "title": title
        })

    df = pd.DataFrame(headlines)

    return df


if __name__ == "__main__":
    print(scrape_news())