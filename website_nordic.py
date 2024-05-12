import requests
from bs4 import BeautifulSoup

# Function to scrape the news items from the website
def scrape_news():
    url = 'https://www.nordicsemi.com/Nordic-news'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all news items
        news_items = soup.find_all('div', class_='post--stacked')
        news_list = []
        for news_item in news_items[:5]:  # Limit to the first 10 news items
            # Extract the news title and date
            news_title = news_item.find('h3', class_='post__title').text.strip()
            news_date = news_item.find('div', class_='post__meta').text.strip()
            # Store the news title and date in a dictionary
            news_list.append({'title': news_title, 'date': news_date})
        return news_list
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

if __name__ == "__main__":
    # Scrape the news items and store them in an array
    news_array = scrape_news()
    if news_array:
        for idx, news in enumerate(news_array, start=1):
            print(f"News {idx}:")
            print("Title:", news['title'])
            print("Date:", news['date'])
            print()
    else:
        print("No news found.")
