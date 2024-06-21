import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.businesswire.com/portal/site/home/news/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all list items
items = soup.find_all('li')

entries = []

# Iterate over each list item to extract title and date
for item in items[:5]:
    title_tag = item.find('span', itemprop='headline')
    date_tag = item.find('time', itemprop='dateModified')
    
    if title_tag and date_tag:
        title = title_tag.get_text(strip=True)
        date = date_tag.get_text(strip=True)
        entries.append((title, date))

# Print the extracted entries
for title, date in entries:
    print(f"Title: {title}, Date: {date}")
