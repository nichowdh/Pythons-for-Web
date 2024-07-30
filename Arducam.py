import requests
from bs4 import BeautifulSoup


def scrape_latest_news(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all articles
        articles = soup.find_all('article')
        
        # Iterate over each article
        for article in articles[:3]:
            # Extract entry title
            entry_title = article.find('h2', class_='entry-title').text.strip()
            
            # Extract published date
            published_date = article.find('span', class_='published').text.strip()
            
            # Print the extracted data
            print("Entry Title:", entry_title)
            print("Published Date:", published_date)
            print()

# URL of the web page to scrape
url = "https://www.arducam.com/blog/"

# Scrape the latest 5 news articles with a dates
latest_news = scrape_latest_news(url)

# Print the scraped news articles
for news in latest_news:
    print(news)
