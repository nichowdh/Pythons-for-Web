import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.digi.com/company/press-releases")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all entries
entries = soup.find_all('div', class_='item')

# Extract title and date for each entry
for entry in entries:
    title = entry.find('h3').text.strip()
    date = entry.find('span', class_='date').text.strip()
    print(f"Title: {title}")
    print(f"Date: {date}")
    print("---")
