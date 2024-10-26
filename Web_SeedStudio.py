import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.seeedstudio.com/blog/news-center/")



# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')


# Find all article elements
articles = soup.find_all('article', class_='elementor-post')

# Extract titles
for article in articles[:3]:
    title_elem = article.find('h3', class_='elementor-post__title').find('a')
    if title_elem:
        title = title_elem.text.strip()
        print(f"Title: {title}")
