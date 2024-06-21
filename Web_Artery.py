from googletrans import Translator
import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.arterychip.com/en/news/index.jsp")

# Initialize the translator
translator = Translator()

soup = BeautifulSoup(response.content, 'html.parser')

entries = []

for item in soup.find_all('div', class_='row blog-item'):
    title = item.find('h3', class_='post-title pt1').text.strip()
    date = item.find('span', class_='date').text.strip()
    # Translate title to English
    translated_title = translator.translate(title, src='auto', dest='en').text
    entries.append({'title': translated_title, 'date': date})

for entry in entries:
    print(f"Title: {entry['title']}")
    print(f"Date: {entry['date']}\n")