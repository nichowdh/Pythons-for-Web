import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://ahlendorf-news.com/en/overview/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

entries = []

for article in soup.find_all('article'):
    title = article.find('h4', class_='media-heading').text.strip()
    date = article.find('div', class_='media-body').find_all('p')[-1].text.strip().split(',')[-1].strip()
    entries.append({'title': title, 'date': date})

for entry in entries:
    print(f"Title: {entry['title']}")
    print(f"Date: {entry['date']}\n")
