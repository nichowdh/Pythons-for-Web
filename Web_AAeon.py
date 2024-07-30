import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.aaeon.com/en/nc/product-news/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all entries
entries = soup.find_all('div', class_='cf iLB')

# Print the entry titles and dates
for i, entry in enumerate(entries[:3]):  # Limit to first  entries
    title_tag = entry.find('h3')
    title = title_tag.get_text(strip=True) if title_tag else 'No title'
    date_tag = entry.find('span', class_='date')
    date = date_tag.get_text(strip=True) if date_tag else 'No date'
    print(f"Title: {title}")
    print(f"Date: {date}\n")
