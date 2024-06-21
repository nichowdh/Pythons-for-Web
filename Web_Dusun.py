import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.dusuniot.com/news/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

titles = []
for article in soup.find_all('article', class_='elementor-post'):
    title_tag = article.find('h3', class_='elementor-post__title')
    if title_tag and title_tag.a:
        titles.append(title_tag.a.text.strip())

for title in titles:
    print(title)
