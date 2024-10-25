import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.luckfox.com/index.php?route=product/catalog'

# Sending a request to fetch the HTML content (use headers if needed)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all product containers
    products = soup.select('.product-layout')
    
    # List to store the parsed entries
    parsed_entries = []
    
    # Extract the first 3 product titles and prices
    for product in products[:3]:  # Limiting to 3 entries
        # Extract title and price
        title = product.select_one('.name a').text.strip()
        price = product.select_one('.price-normal').text.strip()
        
        # Store each entry in a dictionary
        parsed_entries.append({
            'title': title,
            'price': price
        })
    
    # Print out the parsed entries
    for i, entry in enumerate(parsed_entries, 1):
        print(f"Entry {i}:")
        print(f"Title: {entry['title']}")
        print(f"Price: {entry['price']}")
        print()
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
