import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://atreyo.in/index.php/en/resources/blog")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
entries = []

# Find all list items with class 'grid'
for item in soup.find_all('li', class_='grid'):
    title_tag = item.find('h4', class_='blog-title-views').find('span')
    
    if title_tag:
        title = title_tag.get_text(strip=True)
        entries.append(title)

# Print the titles
for title in entries:
    print(f"Title: {title}")
