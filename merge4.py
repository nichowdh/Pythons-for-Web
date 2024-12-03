import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import pandas as pd
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

    # 1. Seeed Studio
    url = "https://www.seeedstudio.com/blog/news-center/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article', class_='elementor-post')[:3]
        for article in articles:
            title = article.find('h3', class_='elementor-post__title').find('a').text.strip()
            date = article.find('span', class_='elementor-post-date').text.strip()
            news_data.append({'Title': title, 'Date': date, 'Source': 'Seeed Studio'})

    # 2. SunFounder
    url = "https://www.sunfounder.com/blogs/news"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='block-list__item-blog')
        for article in articles[:3]:
            title = article.find('h2', class_='article-item__title').find('a').text.strip()
            date = article.find('time', class_='article-item__meta-item').text.strip()
            news_data.append({'Title': title, 'Date': date, 'Source': 'SunFounder'})

    # 3. Synaptics
    url = "https://www.synaptics.com/company/newsroom"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('li', class_='company-newsroom-row')
    for item in items[:3]:
        title = item.find('a', class_='desc_anchor').text.strip()
        date = item.find('time').text.strip()
        news_data.append({'Title': title, 'Date': date, 'Source': 'Synaptics'})

    # 4. FLIR
    url = "https://www.flir.in/news-center/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', class_='Grid-cell u-sm-size1of2 u-md-size1of4')
    for article in articles[:3]:
        title = article.find('h4', class_='Article-title').text.strip()
        news_data.append({'Title': title, 'Date': 'N/A', 'Source': 'FLIR'})

    # 5. Terra Master
    url = "https://www.terra-master.com/global/press/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news_items = soup.find_all('div', class_='news_list_item')
    for item in news_items[:3]:
        title = item.find('a').text.strip() if item.find('a') else 'No title found'
        date = item.find('div', class_='news_item_subtitle').text.split('//')[0].strip() if item.find('div',
                                                                                                          class_='news_item_subtitle') else 'No date found'
        news_data.append({'Title': title, 'Date': date, 'Source': 'Terra Master'})

    # 6. Toradex
    url = "https://www.toradex.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='item d-flex')
    for entry in entries[:3]:
        date = entry.find('div', class_='date').span.text.strip()
        title = entry.find('h5').text.strip()
        additional_text = entry.find('div', class_='card-text').find('p')
        if additional_text:
            title += additional_text.text.strip()
        news_data.append({'Title': title, 'Date': date, 'Source': 'Toradex'})

    # Vecow
    url_vecow = "https://www.vecow.com/dispPageBox/vecow/VecowCP.aspx?ddsPageID=NEWS_EN"
    response = requests.get(url_vecow)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        list_items = soup.find_all('li')
        for item in list_items[:3]:
            title_div = item.find('div', class_='Title')
            date_div = item.find('div', class_='Date')
            if title_div and date_div:
                title = title_div.get_text(strip=True)
                date = date_div.get_text(strip=True)
                news_data.append({'Source': 'Vecow', 'Title': title, 'Date': date})

    # Youyeetoo
    url_youyeetoo = "https://www.youyeetoo.com/blog/"
    response = requests.get(url_youyeetoo)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        blog_items = soup.find_all('div', class_='blog_item')
        for item in blog_items[:3]:
            date_tag = item.find('div', class_='date')
            title_tag = item.find('div', class_='title')
            date = date_tag.text.strip() if date_tag else 'No date found'
            title = title_tag.text.strip() if title_tag else 'No title found'
            news_data.append({'Source': 'Youyeetoo', 'Title': title, 'Date': date})

    # Zeus
    url_zeus = "https://zeus.ugent.be/blog/23-24/"
    response = requests.get(url_zeus)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for blog_preview in soup.find_all('div', class_='content blog-preview')[:3]:
            title_tag = blog_preview.find('a', class_='title')
            date_tag = blog_preview.find('small', class_='column blogpreview-extra')
            title = title_tag.text.strip() if title_tag else 'No title'
            date = date_tag.text.split(' • ')[0].strip() if date_tag else 'No date'
            news_data.append({'Source': 'Zeus', 'Title': title, 'Date': date})

    # Murata
    url_murata = "https://corporate.murata.com/en-global/newsroom"
    response = requests.get(url_murata)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        news_div = soup.find('div', class_='c-news')
        if news_div:
            news_items = news_div.find_all('li', class_='c-news__item')
            for item in news_items[:3]:
                date_elem = item.find('time')
                date = date_elem['datetime'] if date_elem else "No date found"
                title_elem = item.find('div', class_='c-news__text')
                title = title_elem.text.strip() if title_elem else "No title found"
                news_data.append({'Source': 'Murata', 'Title': title, 'Date': date})

    # Variscite
    url_variscite = "https://www.variscite.com/system-on-module-blog/"
    response = requests.get(url_variscite)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        post_items = soup.find_all('div', class_='post-item')
        for post_item in post_items[:3]:
            title = post_item.find('h2', itemprop='name headline').text.strip()
            date = post_item.find('div', class_='date').text.strip()
            news_data.append({'Source': 'Variscite', 'Title': title, 'Date': date})

    # Nuvoton
    url_nuvoton = "https://www.nuvoton.com/news/news/all/"
    response = requests.get(url_nuvoton)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('div', class_='css_tr')
        for row in rows[:4]:
            cells = row.find_all('div', class_='css_td')
            if len(cells) >= 2:
                date = cells[0].get_text(strip=True)
                title_tag = cells[1].find('a')
                if title_tag:
                    title = title_tag.get('title', '').replace('&quot;', '"')
                    news_data.append({'Source': 'Nuvoton', 'Title': title, 'Date': date})

    # Formuler
    url_formuler = "https://www.formuler.tv/news"
    response = requests.get(url_formuler)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article', {'data-hook': 'post-list-item'})
        for article in articles[:3]:
            title_tag = article.find('div', {'data-hook': 'post-title'})
            date_tag = article.find('span', {'data-hook': 'time-ago'})
            if title_tag and date_tag:
                title = title_tag.get_text(strip=True)
                date = date_tag.get_text(strip=True)
                news_data.append({'Source': 'Formuler', 'Title': title, 'Date': date})

    # Quectel
    url_quectel = "https://www.quectel.com/company/news-and-pr/"
    response = requests.get(url_quectel)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('a', class_='group text-black no-underline')
        for article in articles[:3]:
            title = article.find('span', class_='text-lg text-black mb-3').text.strip()
            news_data.append({'Source': 'Quectel', 'Title': title, 'Date': 'No date provided'})

    return news_data


# Scrape news entries
news_entries = scrape_news()

# Create a pandas DataFrame
df = pd.DataFrame(news_entries)

# Print the results to the terminal with a 2-second delay between each
for entry in news_entries:
    print(f"Source: {entry['Source']}")
    print(f"Title: {entry['Title']}")
    print(f"Date: {entry['Date']}")
    print()
    time.sleep(2)  # Pause for 2 seconds between each output


# Write data to an Excel file
df.to_excel('Merge_4.xlsx', index=False, engine='openpyxl')

print("\nData has been written to scraped_news.xlsx")
