import time
import requests
from bs4 import BeautifulSoup
from googletrans import Translator


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

    # Artery Chip News with Translation
    url = "https://www.arterychip.com/en/news/index.jsp"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        translator = Translator()
        for item in soup.find_all('div', class_='row blog-item')[:3]:
            title = item.find('h3', class_='post-title pt1').text.strip()
            date = item.find('span', class_='date').text.strip()
            translated_title = translator.translate(title, src='auto', dest='en').text
            news_data.append({'source': 'Artery Chip', 'title': translated_title, 'date': date})
    else:
        print(f"Failed to retrieve Artery Chip content. Status code: {response.status_code}")

     # Atreyo Blog
    url = "https://atreyo.in/index.php/en/resources/blog"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for item in soup.find_all('li', class_='grid')[:3]:
            title_tag = item.find('h4', class_='blog-title-views').find('span')
            if title_tag:
                title = title_tag.get_text(strip=True)
                news_data.append({'source': 'Atreyo', 'title': title, 'date': "No date found"})
    else:
        print(f"Failed to retrieve Atreyo content. Status code: {response.status_code}")

    # BeagleBoard
    url = "https://www.beagleboard.org/blog/"
    response1 = requests.get(url)
    soup1 = BeautifulSoup(response1.content, 'html.parser')
    entries1 = soup1.find_all('div', class_='feature-card')
    for entry in entries1[:3]:
        title_element = entry.find('p', class_='card-title')
        title = title_element.text.strip() if title_element else "No title found"
        news_data.append({'source': 'BeagleBoard', 'title': title, 'date': 'No date found'})

    # BusinessWire
    url = "https://www.businesswire.com/portal/site/home/news/"
    response2 = requests.get(url)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    items2 = soup2.find_all('li')
    for item in items2[:3]:
        title_tag = item.find('span', itemprop='headline')
        date_tag = item.find('time', itemprop='dateModified')
        if title_tag and date_tag:
            title = title_tag.get_text(strip=True)
            date = date_tag.get_text(strip=True)
            news_data.append({'source': 'BusinessWire', 'title': title, 'date': date})

    # Collabora
    url = "https://www.collabora.com/news-and-blog/"
    response3 = requests.get(url)
    soup3 = BeautifulSoup(response3.content, 'html.parser')
    entries3 = soup3.find_all('div', class_='BlogAndNewsArticleTplWrapper')
    for entry in entries3[:3]:
        title_tag = entry.find('h3').find('a')
        date_tag = entry.find('p', class_='_2016datestamp').find('strong')
        title = title_tag.get_text(strip=True) if title_tag else "No title found"
        date = date_tag.get_text(strip=True) if date_tag else "No date found"
        news_data.append({'source': 'Collabora', 'title': title, 'date': date})

    # Coral
    url = "https://coral.ai/news/"
    response4 = requests.get(url)
    soup4 = BeautifulSoup(response4.content, 'html.parser')
    articles4 = soup4.find_all('article', class_='home-tile')
    for article in articles4[:3]:
        entry_title_element = article.find('h2', class_='home-external-tile__header__big-title')
        entry_title = entry_title_element.text.strip() if entry_title_element else "No title found"
        date_element = article.find('span', class_='home-external-tile__content__date')
        date = date_element.text.strip() if date_element else "No date found"
        news_data.append({'source': 'Coral', 'title': entry_title, 'date': date})

    # CTL Insights
    url = "https://ctl.net/blogs/insights"
    response5 = requests.get(url)
    soup5 = BeautifulSoup(response5.content, 'html.parser')
    article_items5 = soup5.find_all('div', class_='article-item')
    for item in article_items5[:3]:
        title_tag = item.find('h3', class_='article-item__title')
        date_tag = item.find('time', class_='article__meta-item article__date')
        title = title_tag.get_text(strip=True) if title_tag else "No title found"
        date = date_tag.get_text(strip=True) if date_tag else "No date found"
        news_data.append({'source': 'CTL Insights', 'title': title, 'date': date})

    # DF Robot
    url = "https://www.dfrobot.com/blog"
    response6 = requests.get(url)
    soup6 = BeautifulSoup(response6.content, 'html.parser')
    titles6 = [title.text.strip() for title in soup6.find_all('a', class_='title')][:3]
    for title in titles6:
        news_data.append({'source': 'DF Robot', 'title': title, 'date': 'No date found'})

    # Digi Press Releases
    url = "https://www.digi.com/company/press-releases"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('div', class_='item')
        for entry in entries[:3]:
            title = entry.find('h3').text.strip()
            date = entry.find('span', class_='date').text.strip()
            news_data.append({'source': 'Digi', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve Digi content. Status code: {response.status_code}")

    # DusunIoT News
    url = "https://www.dusuniot.com/news/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article', class_='elementor-post')
        for article in articles[:3]:
            title_tag = article.find('h3', class_='elementor-post__title')
            if title_tag and title_tag.a:
                title = title_tag.a.text.strip()
                news_data.append({'source': 'DusunIoT', 'title': title, 'date': 'No date'})
    else:
        print(f"Failed to retrieve DusunIoT content. Status code: {response.status_code}")

    # ECSIPC News
    url = "https://www.ecsipc.com/en/news"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('div', class_='item')
        for entry in entries[:3]:
            date_tag = entry.find('div', class_='tag-date').find('span', class_='name')
            date = date_tag.get_text(strip=True) if date_tag else 'No date'
            title_tag = entry.find('h4').find('a', class_='title')
            title = title_tag.get_text(strip=True) if title_tag else 'No title'
            news_data.append({'source': 'ECSIPC', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve ECSIPC content. Status code: {response.status_code}")

    # Edatec Products
    url = "https://www.edatec.cn/en/product/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.select('.blog-article')
        for article in articles[:3]:
            title = article.select_one('.entry-title a').text.strip()
            date = article.select_one('.entry-date time').get('datetime').strip()
            news_data.append({'source': 'Edatec', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve Edatec content. Status code: {response.status_code}")

    # Edge Impulse Blog
    url = "https://edgeimpulse.com/blog/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('article', class_='flex')
        for entry in entries[:3]:
            title = entry.find('h3').text.strip()
            date = entry.find('time')['datetime']
            news_data.append({'source': 'Edge Impulse', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve Edge Impulse content. Status code: {response.status_code}")

    # Elecrow News
    url = "https://www.elecrow.com/blog/elecrow-news"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        posts = soup.find_all('li', class_='post-item')
        for post in posts[:3]:
            title = post.find('h3', class_='post-title').get_text(strip=True)
            date = post.find('span', class_='post-date').get_text(strip=True)
            news_data.append({'source': 'Elecrow', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve Elecrow content. Status code: {response.status_code}")

    # Firefly News
    url = "https://en.t-firefly.com/news.html"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('div', class_='news-list')
        for entry in entries[:3]:
            title_tag = entry.find('h4').find('a')
            title = title_tag.get_text(strip=True) if title_tag else 'No title'
            date_tag = entry.find('div', class_='other').find('span')
            date = date_tag.get_text(strip=True) if date_tag else 'No date'
            news_data.append({'source': 'Firefly', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve Firefly content. Status code: {response.status_code}")

    # Print the news data
    for entry in news_data:
        print(f"Source: {entry['source']}")
        print(f"Title: {entry['title']}")
        print(f"Date: {entry['date']}\n")
        time.sleep(2)

# Run the function
scrape_news()
