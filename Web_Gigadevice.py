import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.gigadevice.com/about/news-and-event/news")


soup = BeautifulSoup(response.content, 'html.parser')

# Find all the entries
entries = soup.find_all('div', class_='he_h2p2hul clearfix')

for entry in entries:
    # Extract all individual articles within each entry
    articles = entry.find_all('div', class_='he_h2p2hli fl')

    for article in articles:
        # Extract the date
        date = article.find('div', class_='he_h2p2htim').p.text.strip()
        # Extract the title
        title = article.find('div', class_='he_h2p2hxp').p.text.strip()

        # Print the extracted information
        print(f"Date: {date}")
        print(f"Title: {title}")
        print('-' * 50)
