import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.ecsipc.com/en/news")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

items = soup.select('.container .item')

for item in items:
    date = item.select_one('.tag-date .name').text.strip()
    title = item.select_one('h4 .title').text.strip()
    print(f"Date: {date}, Title: {title}")
