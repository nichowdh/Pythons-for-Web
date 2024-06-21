import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.ambarella.com/news-events/"

# Custom headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request to the URL with custom headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.select('article.news')

    for article in articles:
        title_tag = article.select_one('.news-title a')
        date_tag = article.select_one('time.news-published')
        
        if title_tag and date_tag:
            title = title_tag.text.strip()
            date = date_tag.get('datetime').split('T')[0]
            print(f"Date: {date}, Title: {title}")
        else:
            print("Title or date not found for an article.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
