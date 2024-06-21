import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://news.samsung.com/global/latest")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <li> elements inside <ul class="item">
entries = soup.find('ul', class_='item').find_all('li')

# Iterate through each <li> to extract title and date
for entry in entries:
    title = entry.find('span', class_='title').text.strip()
    date = entry.find('span', class_='date').text.strip()
    print(f"Title: {title}\nDate: {date}\n")
