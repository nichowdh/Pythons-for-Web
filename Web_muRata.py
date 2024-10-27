import requests
from bs4 import BeautifulSoup

url = "https://corporate.murata.com/en-global/newsroom"  # Replace with your actual URL

try:
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <div> with class="c-news"
    news_div = soup.find('div', class_='c-news')

    if news_div:
        # Find all <li> elements inside the <ul> with class="c-news__items"
        news_items = news_div.find_all('li', class_='c-news__item')

        for item in news_items[:3]:
            # Extract date
            date_elem = item.find('time')
            date = date_elem['datetime'] if date_elem else "No date found"

            # Extract title
            title_elem = item.find('div', class_='c-news__text')
            title = title_elem.text.strip() if title_elem else "No title found"

            print(f"Title: {title}\nDate: {date}\n")

    else:
        print("No news items found on the page.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching page: {e}")

except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
