import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://www.flir.in/news-center/"
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all div elements with class="Grid-cell u-sm-size1of2 u-md-size1of4"
articles = soup.find_all('div', class_='Grid-cell u-sm-size1of2 u-md-size1of4')

# Iterate through each article to extract title and link
for article in articles:
    # Extract title
    title = article.find('h4', class_='Article-title').text.strip()
    
    print(f"Title: {title}")
   
