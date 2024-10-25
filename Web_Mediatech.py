import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://corp.mediatek.com/news-events/press-releases"

try:
    # Send a GET request to the URL with SSL verification disabled
    response = requests.get(url, verify=False)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all article elements
    articles = soup.find_all('article', class_='entry-content block')

    # Extract titles and dates
    for article in articles[:3]:
        title_tag = article.find('h3')
        date_tag = article.find('span', class_='date')
        
        if title_tag and date_tag:
            title = title_tag.get_text(strip=True)
            date = date_tag.get_text(strip=True)
            print(f'Title: {title}')
            print(f'Date: {date}')
            print()

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
