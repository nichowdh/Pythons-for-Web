import requests
from bs4 import BeautifulSoup

url = "https://www.ambarella.com/news-events/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all articles
    articles = soup.find_all('article', class_='news')

    for article in articles[:3]:
        news_title = article.find('h2', class_='news-title').text.strip()
        news_date = article.find('time', class_='news-published')['datetime']

        print(f"Title: {news_title}")
        print(f"Date: {news_date}")
        print()

except requests.exceptions.RequestException as e:
    print(f"Error fetching content: {e}")
except Exception as e:
    print(f"Error: {e}")
