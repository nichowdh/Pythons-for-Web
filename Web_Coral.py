import requests
from bs4 import BeautifulSoup

url = "https://coral.ai/news/"

# Send a GET request to the URL
response = requests.get(url)

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all articles with class "home-tile"
articles = soup.find_all('article', class_='home-tile')

# Loop through each article
for article in articles:
    # Extract entry title
    entry_title_element = article.find('h2', class_='home-external-tile__header__big-title')
    entry_title = entry_title_element.text.strip() if entry_title_element else "Entry title not found"

    # Extract date
    date_element = article.find('span', class_='home-external-tile__content__date')
    date = date_element.text.strip() if date_element else "Date not found"

    # Extract publish class
    publish_class_element = article.find('span', class_='home-external-tile__header__site-name')
    publish_class = publish_class_element.text.strip() if publish_class_element else "Publish class not found"

    # Print the extracted information
    print(f"Entry Title: {entry_title}")
    print(f"Date: {date}")
    print(f"Publish Class: {publish_class}")
    print("=" * 50)
