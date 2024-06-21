import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.edatec.cn/en/product/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.select('.blog-article')

for article in articles:
    title = article.select_one('.entry-title a').text.strip()
    date = article.select_one('.entry-date time').get('datetime').strip()
    print(f"Date: {date}, Title: {title}")
