import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.variscite.com/system-on-module-blog/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <div> elements with class "post-item"
post_items = soup.find_all('div', class_='post-item')

# Iterate through each post item to extract title and date
for post_item in post_items[:3]:
    # Extract title
    title = post_item.find('h2', itemprop='name headline').text.strip()
    
    # Extract date
    date = post_item.find('div', class_='date').text.strip()
    
    print(f"Title: {title}\nDate: {date}\n")
