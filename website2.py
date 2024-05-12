import requests
from bs4 import BeautifulSoup
import threading

# Function to scrape the latest news from the website
def scrape_latest_news():
    url = 'https://www.nuvoton.com/news/news/all/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.find_all('a', class_='news-item-link')
        latest_news = [item.text.strip() for item in news_items]
        return latest_news
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

# Global variable to store the latest news
latest_news = []

# Function to continuously check for updates
def check_for_updates():
    global latest_news
    while True:
        new_news = scrape_latest_news()
        if new_news:
            if new_news != latest_news:
                print("Latest news detected!")
                print("Old news:", latest_news)
                print("New news:", new_news)
                latest_news = new_news
        else:
            print("No latest news found.")
        # Sleep for 1 minute before checking again
        threading.Timer(60, check_for_updates).start()

if __name__ == "__main__":
    # Start the thread to continuously check for updates
    check_for_updates()
