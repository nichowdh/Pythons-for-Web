import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://norvi.lk/blog/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all article elements
articles = soup.find_all('article')

entries = []

# Iterate over the first 3 articles to extract the title and date
for article in articles[:5]:
    title_tag = article.find('h3', class_='elementor-post__title').find('a')
    date_tag = article.find('span', class_='elementor-post-date')
    
    if title_tag and date_tag:
        title = title_tag.get_text(strip=True)
        date = date_tag.get_text(strip=True)
        entries.append((title, date))

# Print the extracted entries
for title, date in entries:
    print(f"Title: {title}, Date: {date}")
