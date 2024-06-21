import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.seeedstudio.com/blog/news-center/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the first three articles
articles = soup.find_all('article', class_='elementor-post')[:5]

# Iterate through the articles and extract the required information
for article in articles:
    title_element = article.find('h3', class_='elementor-post__title').find('a')
    title = title_element.text.strip()
    date = article.find('span', class_='elementor-post-date').text.strip()
    
    print(f"Title: {title}")
    print(f"Date: {date}")
    print()
