import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://newsroom.arm.com/news")


# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all ads-card elements
cards = soup.find_all('ads-card')

# Extract titles and dates
for card in cards:
    title = card.find('h3', class_='PostAnnounce__title').get_text(strip=True)
    date = card.find('ads-breadcrumb', class_='PostAnnounce__date').get_text(strip=True)
    print(f'Title: {title}')
    print(f'Date: {date}')
    print()
    