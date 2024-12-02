import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import time


def scrape_news():
    news_data = []

    # Sapphire Technology
    url1 = "https://www.sapphiretech.com/en/news"
    response1 = requests.get(url1)
    soup1 = BeautifulSoup(response1.content, 'html.parser')
    list_items = soup1.find_all('div', class_='listItem')
    for item in list_items[:3]:
        date = item.find('time').text.strip() if item.find('time') else 'No date found'
        title = item.find('h3').text.strip() if item.find('h3') else 'No title found'
        news_data.append({'Source': 'Sapphire Technology', 'Title': title, 'Date': date})

    # Seeed Studio
    url2 = "https://www.seeedstudio.com/blog/news-center/"
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    articles = soup2.find_all('article', class_='elementor-post')
    for article in articles[:3]:
        title_elem = article.find('h3', class_='elementor-post__title').find('a')
        title = title_elem.text.strip() if title_elem else 'No title found'
        news_data.append({'Source': 'Seeed Studio', 'Title': title, 'Date': 'No date found'})

    # SiFive
    url3 = "https://www.sifive.com/press"
    response3 = requests.get(url3)
    soup3 = BeautifulSoup(response3.content, 'html.parser')
    for article in soup3.find_all('div', class_='PressReleases_article__Ca53e')[:3]:
        date = article.find('p').text.split('—')[-1].strip() if article.find('p') else 'No date found'
        title_tag = article.find('a', class_='PressReleases_titleLink__T_E_d')
        title = title_tag.text.strip() if title_tag else 'No title found'
        news_data.append({'Source': 'SiFive', 'Title': title, 'Date': date})

    # SmartCow
    url4 = "https://www.smartcow.ai/press-releases-home"
    response4 = requests.get(url4)
    soup4 = BeautifulSoup(response4.content, 'html.parser')
    entries = soup4.find_all('div', class_='w-dyn-item')
    for entry in entries[:3]:
        title_tag = entry.find('h1', class_='display-s-light')
        date_tag = entry.find('div', class_='text-m-reg has--n700-text')
        title = title_tag.get_text(strip=True) if title_tag else 'No title found'
        date = date_tag.get_text(strip=True) if date_tag else 'No date found'
        news_data.append({'Source': 'SmartCow', 'Title': title, 'Date': date})

    # SMLight
    url5 = "https://smlight.tech/shop/?orderby=date"
    response5 = requests.get(url5)
    soup5 = BeautifulSoup(response5.content, 'html.parser')
    titles = [h2.text.strip() for h2 in soup5.find_all('h2', class_='woocommerce-loop-product__title')[:3]]
    for title in titles:
        news_data.append({'Source': 'SMLight', 'Title': title, 'Date': 'No date found'})

    # SpaceTouch
    url6 = "https://www.spacetouch.co/cat47"
    response6 = requests.get(url6)
    soup6 = BeautifulSoup(response6.content, 'html.parser')
    translator = Translator()
    entries = soup6.find_all("div", class_="nwom")
    for entry in entries[:3]:
        title_tag = entry.find("div", class_="sim s24")
        if title_tag:
            title = title_tag.get_text(strip=True)
            translated_title = translator.translate(title, src='zh-cn', dest='en').text
            news_data.append({'Source': 'SpaceTouch', 'Title': translated_title, 'Date': 'No date found'})

    # Radxa
    url = "https://radxa.com/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news_items = soup.select('ul.news_TIAz > li')
    for item in news_items[:3]:
        title_tag = item.select_one('div.new_t_gfEZ > h2')
        title = title_tag.text.strip() if title_tag else 'No title found'
        date_tag = item.select_one('p.time_soVr')
        date = date_tag.text.strip() if date_tag else 'No date found'
        news_data.append({'Source': 'Radxa', 'Title': title, 'Date': date})

    # Robustel
    url = "https://www.robustel.com/category/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='list-item')
    for entry in entries[:3]:
        title = entry.find('h1', class_='list-item-title').a.text.strip()
        news_data.append({'Source': 'Robustel', 'Title': title, 'Date': 'No date found'})

    # SD Association
    url = "https://www.sdcard.org/press/whatsnew/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for li in soup.find_all('li')[:3]:
        date_tag = li.find('time', class_='updated entry-time')
        date = date_tag.get('datetime', '').strip() if date_tag else 'No date found'
        title_tag = li.find('span', class_='bold')
        title = title_tag.a.text.strip() if title_tag and title_tag.a else title_tag.text.strip() if title_tag else 'No title found'
        news_data.append({'Source': 'SD Association', 'Title': title, 'Date': date})

    # STMicroelectronics
    url = "https://newsroom.st.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('a', class_='swiper-slide stn-card stn-card--mobile-list')
    for entry in entries[:3]:
        title_tag = entry.find('h3')
        title = title_tag.get_text(strip=True) if title_tag else 'No title found'
        date_tag = entry.find('div', class_='stn-card__date')
        date = date_tag.get_text(strip=True) if date_tag else 'No date found'
        news_data.append({'Source': 'STMicroelectronics', 'Title': title, 'Date': date})

    # Samsung
    url = "https://news.samsung.com/global/latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find('ul', class_='item').find_all('li')
    for entry in entries[:3]:
        title = entry.find('span', class_='title').text.strip()
        date = entry.find('span', class_='date').text.strip()
        news_data.append({'Source': 'Samsung', 'Title': title, 'Date': date})

    return news_data


# Run the function and display results with a 2-second pause between outputs
news_entries = scrape_news()
for entry in news_entries:
    print(f"Source: {entry['Source']}")
    print(f"Title: {entry['Title']}")
    print(f"Date: {entry['Date']}")
    print()
    time.sleep(2)  # Pause for 2 seconds between each output
