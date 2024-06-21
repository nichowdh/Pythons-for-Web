import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.luckfox.com/index.php?route=product/catalog")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
    
# Extract title and price
title = soup.find('div', class_='name').a.get_text(strip=True)
price = soup.find('span', class_='price-normal').get_text(strip=True)
    
print(f"Title: {title}")
print(f"Price: {price}")
print("-" * 30)
