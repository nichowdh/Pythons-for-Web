import requests
from bs4 import BeautifulSoup

# Define the URL
url = 'https://www.aaeon.com/en/news/list/product-news'

# Send a GET request to fetch the page content
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the latest 3 entries
entries = soup.find_all('div', class_='item_cell', limit=3)

# Extract and display the titles and dates
for entry in entries:
    title = entry.find('h3').get_text(strip=True)
    date = entry.find('span', class_='display_date').get_text(strip=True)
    print(f"Title: {title}\nDate: {date}\n")
