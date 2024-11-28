import time
import requests
from bs4 import BeautifulSoup

def scrape_news():
    news_data = []

    # Arducam Blog
    url = "https://www.arducam.com/blog/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles[:3]:
            title = article.find('h2', class_='entry-title').get_text(strip=True)
            date = article.find('span', class_='published').get_text(strip=True)
            news_data.append({'source': 'Arducam', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve Arducam content. Status code: {response.status_code}")


    # Semtech News
    url = "https://www.semtech.com/company/news-and-media"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        cards = soup.find_all('div', class_='col-12 col-md-4 col-match-height')
        for card in cards[:3]:
            title_tag = card.find('p', class_='h5 text-green pt-2 text-start').find('a')
            title = title_tag.get_text(strip=True) if title_tag else "No title found"
            date_tag = card.find('span', class_='entry-meta')
            date = date_tag.get_text(strip=True) if date_tag else "No date found"
            news_data.append({'source': 'Semtech', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve Semtech content. Status code: {response.status_code}")


        # AAEON Product News (list/product-news)
        url = 'https://www.aaeon.com/en/news/list/product-news'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            entries = soup.find_all('div', class_='item_cell', limit=3)
            for entry in entries:
                title = entry.find('h3').get_text(strip=True)
                date = entry.find('span', class_='display_date').get_text(strip=True)
                news_data.append({'source': 'AAEON (list/product-news)', 'title': title, 'date': date})
        else:
            print(f"Failed to retrieve AAEON (list/product-news) content. Status code: {response.status_code}")

    # Ahlendorf News
    url = "https://ahlendorf-news.com/en/overview/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for article in soup.find_all('article')[:3]:
            title = article.find('h4', class_='media-heading').get_text(strip=True)
            date = article.find('div', class_='media-body').find_all('p')[-1].get_text(strip=True).split(',')[-1].strip()
            news_data.append({'source': 'Ahlendorf', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve Ahlendorf content. Status code: {response.status_code}")


    # ARM Newsroom
    url = "https://newsroom.arm.com/news"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        cards = soup.find_all('ads-card')
        for card in cards[:3]:
            title = card.find('h3', class_='PostAnnounce__title').get_text(strip=True) if card.find('h3', class_='PostAnnounce__title') else 'No title'
            date = card.find('ads-breadcrumb', class_='PostAnnounce__date').get_text(strip=True) if card.find('ads-breadcrumb', class_='PostAnnounce__date') else 'No date'
            news_data.append({'source': 'ARM', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve ARM content. Status code: {response.status_code}")




    # Print the news data
    for entry in news_data:
        print(f"Source: {entry['source']}")
        print(f"Title: {entry['title']}")
        print(f"Date: {entry['date']}\n")
        time.sleep(2)

# Run the function
scrape_news()
