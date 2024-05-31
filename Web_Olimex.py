import requests
from bs4 import BeautifulSoup

# For News
# Send a GET request to the URL
response = requests.get("https://www.olimex.com/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

entries = soup.find_all('div', class_='news')

# Print first 3 News entries
print("News")
for index, entry in enumerate(entries[:3], start=1):
    title_tag = entry.find('h2')
    title = title_tag.get_text(strip=True) if title_tag else 'No title'
    date_tag = entry.find('div', class_='details').find('b')
    date = date_tag.get_text(strip=True) if date_tag else 'No date'
    print(f"{index}. Title: {title}")
    print(f"   Date: {date}\n")

# For Products
# Send a GET request to the URL
response1 = requests.get("https://www.olimex.com/Products/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response1.content, 'html.parser')

entries = soup.find_all('div', class_='pricing left')

# Print first 3 Products entries
print("Products")
for index, entry in enumerate(entries[:3], start=1):
    title_tag = entry.find('p')
    title = title_tag.get_text(strip=True) if title_tag else 'No title'
    price_tag = entry.find('div', class_='pricing default')
    price = price_tag.get_text(strip=True) if price_tag else 'Price not found'
    print(f"{index}. Title: {title}")
    print(f"   Price: {price}\n")
