import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.seco.com/blog/news/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

titles = [a.text.strip() for a in soup.find_all('a', href=True) if a.find_parent('h3', class_='elementor-post__title')]

for title in titles:
    print(title)
