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

    # FriendlyElec Forum
    url = "https://www.friendlyelec.com/Forum/viewforum.php?f=3"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr', class_='t-row clickable')
        for row in rows[:3]:
            title_tag = row.find('a', class_='topictitle')
            title = title_tag.text.strip() if title_tag else 'No title found'
            date_tag = row.find('small')
            date = date_tag.text.strip() if date_tag else 'No date found'
            news_data.append({'source': 'FriendlyElec', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve FriendlyElec content. Status code: {response.status_code}")

    # GeekomPC News
    url = "https://community.geekompc.com/forums/official-news-and-deals.38/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        threads = soup.find_all('div', class_='structItem')
        for thread in threads[:3]:
            title_tag = thread.find('div', class_='structItem-title')
            if title_tag:
                title = title_tag.find_all('a')[-1].get_text(strip=True)
                date_tag = thread.find('li', class_='structItem-startDate').find('time')
                date = date_tag.get_text(strip=True) if date_tag else 'No date'
                news_data.append({'source': 'GeekomPC', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve GeekomPC content. Status code: {response.status_code}")

    # GigaDevice News
    url = "https://www.gigadevice.com/about/news-and-event/news"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('div', class_='he_h2p2hul clearfix')
        for entry in entries:
            articles = entry.find_all('div', class_='he_h2p2hli fl')
            for article in articles[:3]:
                date = article.find('div', class_='he_h2p2htim').p.text.strip() if article.find('div',
                                                                                                class_='he_h2p2htim') else 'No date'
                title = article.find('div', class_='he_h2p2hxp').p.text.strip() if article.find('div',
                                                                                                class_='he_h2p2hxp') else 'No title'
                news_data.append({'source': 'GigaDevice', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve GigaDevice content. Status code: {response.status_code}")

    # Elegoo Blog
    url = "https://www.elegoo.com/pages/blog-collection#3d"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        blog_posts = soup.find_all('div', class_='blog-post')
        for post in blog_posts[:3]:
            title = post.find('h5').get_text(strip=True) if post.find('h5') else 'No title'
            date = post.find('aside', class_='post-meta').get_text(strip=True) if post.find('aside',
                                                                                            class_='post-meta') else 'No date'
            news_data.append({'source': 'Elegoo', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve Elegoo content. Status code: {response.status_code}")

    # GetTobyte Semiconductor Blogs
    url = "https://gettobyte.com/semiconductor-chip-blogs/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('div', class_='serv-box-2 s2')
        for entry in entries[:3]:
            title = entry.find('h5').text.strip() if entry.find('h5') else 'No title'
            news_data.append({'source': 'GetTobyte', 'title': title, 'date': 'No date'})
    else:
        print(f"Failed to retrieve GetTobyte content. Status code: {response.status_code}")

        # Hubitat Blog

    # scrape_hubitat
    url = "https://hubitat.com/blog"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('div', class_='BlogItem_item__OCiDd')
        for entry in entries[:3]:
            title = entry.find('h2', class_='BlogItem_title__9_nUp').get_text(strip=True) if entry.find('h2',
                                                                                                            class_='BlogItem_title__9_nUp') else 'No title'
            date = entry.find('p', class_='BlogItem_date__NaQEt').get_text(strip=True) if entry.find('p',
                                                                                                         class_='BlogItem_date__NaQEt') else 'No date'
            news_data.append({'source': 'Hubitat', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve Hubitat content. Status code: {response.status_code}")

    # scrape_jetway
    url = "https://jetwayipc.com/jetwaynews/?lang=en"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        post_items = soup.find_all('div', class_='post-item')
        for item in post_items[:3]:
            title = item.find('h5', class_='post-title').text.strip() if item.find('h5',
                                                                                   class_='post-title') else 'No title'
            news_data.append({'source': 'Jetway IPC', 'title': title, 'date': 'No date'})
    else:
        print(f"Failed to retrieve jetway content. Status code: {response.status_code}")

    # scrape_m5stack
    url = "https://m5stack.com/explore?page=1"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        news_cards = soup.find_all('div', class_='news-card')
        for card in news_cards[:3]:
            title = card.find('div', class_='news-card-title').find('a').text.strip() if card.find('div',
                                                                                                   class_='news-card-title').find(
                'a') else 'No title'
            date = card.find('div', class_='news-card-date').text.strip() if card.find('div',
                                                                                       class_='news-card-date') else 'No date'
            news_data.append({'source': 'M5Stack', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve m5stack content. Status code: {response.status_code}")


    # scrape_makerfabs
    url = "https://www.makerfabs.com/blog"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('div', class_='post-item')
        for item in items[:3]:
            title = item.find('span', class_='post-title').get_text(strip=True) if item.find('span',
                                                                                             class_='post-title') else 'No title'
            date = item.find('div', class_='post-posed-date').get_text(strip=True) if item.find('div',
                                                                                                class_='post-posed-date') else 'No date'
            news_data.append({'source': 'Makerfabs', 'title': title, 'date': date})
    else:
        print(f"Failed to retrieve makerfabs content. Status code: {response.status_code}")

    # The Minix Forum News
    url = "https://theminixforum.com/index.php?forums/news-announcements.2/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    struct_items = soup.find_all('div', class_='structItem')
    for item in struct_items[:3]:
        title_tag = item.find('div', class_='structItem-title').find('a')
        date_tag = item.find('li', class_='structItem-startDate').find('time')
        news_data.append({
            "source": "The Minix Forum",
            "title": title_tag.text.strip(),
            "date": date_tag['datetime']
        })

    # NXP Newsroom
    url = "https://www.nxp.com/company/about-nxp/newsroom:NEWSROOM"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='card1-item')
    for entry in entries[:3]:
        title = entry.find('h3', class_='card1-title').text.strip()
        date = entry.find('p', class_='metadata').text.strip()
        news_data.append({
            "source": "NXP",
            "title": title,
            "date": date
        })

    # Norvi Blog
    url = "https://norvi.lk/blog/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')
    for article in articles[:3]:
        title_tag = article.find('h3', class_='elementor-post__title').find('a')
        date_tag = article.find('span', class_='elementor-post-date')
        news_data.append({
            "source": "Norvi",
            "title": title_tag.get_text(strip=True),
            "date": date_tag.get_text(strip=True)
        })

    # Olimex News
    url = "https://www.olimex.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='news')
    for entry in entries[:3]:
        title_tag = entry.find('h2')
        date_tag = entry.find('div', class_='details').find('b')
        news_data.append({
            "source": "Olimex News",
            "title": title_tag.get_text(strip=True) if title_tag else 'No title',
            "date": date_tag.get_text(strip=True) if date_tag else 'No date'
        })

    # Olimex Products
    url = "https://www.olimex.com/Products/"
    response1 = requests.get(url)
    soup = BeautifulSoup(response1.content, 'html.parser')
    entries = soup.find_all('div', class_='pricing left')
    for entry in entries[:3]:
        title_tag = entry.find('p')
        price_tag = entry.find('div', class_='pricing default')
        news_data.append({
            "source": "Olimex Products",
            "title": title_tag.get_text(strip=True) if title_tag else 'No title',
            "date": price_tag.get_text(strip=True) if price_tag else 'Price not found'
        })

    # ON Semiconductor News
    url = "https://www.onsemi.com/company/news-media/in-the-news"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('div', class_='card')
        for entry in entries[:3]:
            date_tag = entry.find('p').find('span')
            title_tag = entry.find('h6').find('a')
            news_data.append({
                "source": "ON Semiconductor",
                "title": title_tag.text if title_tag else 'No title found',
                "date": date_tag.text if date_tag else 'No date found'
            })



    # Print the news data
    for entry in news_data:
        print(f"Source: {entry['source']}")
        print(f"Title: {entry['title']}")
        print(f"Date: {entry['date']}\n")
        time.sleep(2)

# Run the function
scrape_news()
