import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://m5stack.com/explore?page=1")


# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

news_cards = soup.find_all('div', class_='news-card')

entries = []

for card in news_cards:
    title_tag = card.find('div', class_='news-card-title').find('a')
    date_tag = card.find('div', class_='news-card-date')
    
    title = title_tag.text.strip() if title_tag else 'No title'
    date = date_tag.text.strip() if date_tag else 'No date'
    
    entries.append({'title': title, 'date': date})

for entry in entries[:3]:
    print(f"Title: {entry['title']}, Date: {entry['date']}")
