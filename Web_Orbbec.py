import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://shop.orbbec3d.com/shop"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to fetch page: Status code {response.status_code}")
    exit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all div elements with class="facets-items-collection-view-cell-span3"
items = soup.find_all('div', class_='facets-items-collection-view-cell-span3')

# Check if items were found
if not items:
    print("No items found on the page.")
    exit()

# Iterate through each item to extract title and price
for item in items:
    # Extract title
    title_element = item.find('span', itemprop='name')
    if title_element:
        title = title_element.text.strip()
    else:
        title = "Title not found"
    
    # Extract price
    price_element = item.find('span', class_='product-views-price-lead')
    if price_element:
        price = price_element.text.strip()
    else:
        price = "Price not found"
    
    print(f"Title: {title}")
    print(f"Price: {price}\n")
