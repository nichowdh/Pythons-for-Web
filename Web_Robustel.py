import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.robustel.com/category/news/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

entries = soup.find_all('div', class_='list-item')

for entry in entries:
    title = entry.find('h1', class_='list-item-title').a.text.strip()
    print(f"Title: {title}")
