import requests
from bs4 import BeautifulSoup

# URL to fetch
url = "https://www.synaptics.com/company/newsroom"

# Fetch the webpage content
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the list items
items = soup.find_all('li', class_='company-newsroom-row')

# Iterate through each item and extract the title and date
for item in items[:3]:
    date_tag = item.find('time')
    title_tag = item.find('a', class_='desc_anchor')
    
    if date_tag and title_tag:
        date = date_tag.get_text(strip=True)
        title = title_tag.get_text(strip=True)
        print(f"Date: {date}")
        print(f"Title: {title}")
        print()
