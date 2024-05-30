from bs4 import BeautifulSoup
import requests

# Send a GET request to the URL
response = requests.get("https://www.renesas.com/us/en/about/newsroom#latest-press-releases")



# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all items with class 'item-wrapper press-releases-item-wrapper'
items = soup.find_all('div', class_='item-wrapper press-releases-item-wrapper')

# Loop through each item and extract title and date
for item in items:
    # Extract title
    title = item.find('div', class_='item-title press-releases-item-title').text.strip()
    
    # Extract date
    date = item.find('time', class_='datetime press-releases-datetime')['datetime']
    
    print(f"Title: {title}")
    print(f"Date: {date}")
    print("-" * 20)
