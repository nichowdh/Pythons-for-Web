from bs4 import BeautifulSoup
import requests

def scrape_latest_news(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all articles
        articles = soup.find_all('article')

        # List to store the news
        news_list = []

        # Iterate over each article (limit to the first 3)
        for article in articles[:3]:
            # Extract entry title
            entry_title = article.find('h2', class_='entry-title').text.strip()

            # Extract published date
            published_date = article.find('span', class_='published').text.strip()

            # Append the extracted data to the news list
            news_list.append({
                'Entry Title': entry_title,
                'Published Date': published_date
            })

        # Return the list of news articles
        return news_list
    else:
        print(f"Failed to retrieve the content. Status code: {response.status_code}")
        return []

# URL of the web page to scrape
url = "https://www.arducam.com/blog/"

# Scrape the latest 3 news articles with their dates
latest_news = scrape_latest_news(url)

# Print the scraped news articles
for news in latest_news:
    print(f"Entry Title: {news['Entry Title']}")
    print(f"Published Date: {news['Published Date']}")
    print()
