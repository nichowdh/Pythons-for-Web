import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def fetch_m5stack():
    response = requests.get("https://m5stack.com/explore?page=1")
    soup = BeautifulSoup(response.content, 'html.parser')
    news_cards = soup.find_all('div', class_='news-card')

    entries = []
    for card in news_cards[:3]:
        title_tag = card.find('div', class_='news-card-title').find('a')
        date_tag = card.find('div', class_='news-card-date')
        title = title_tag.text.strip() if title_tag else 'No title'
        date = date_tag.text.strip() if date_tag else 'No date'
        entries.append({'title': title, 'date': date})

    print("M5Stack News:")
    for entry in entries:
        print(f"Title: {entry['title']}, Date: {entry['date']}")
    print("\n")
    time.sleep(2)


def fetch_makerfabs():
    response = requests.get("https://www.makerfabs.com/blog")
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_='post-item')

    print("Makerfabs Blog:")
    for item in items[:3]:
        title_tag = item.find('span', class_='post-title')
        date_tag = item.find('div', class_='post-posed-date')
        title = title_tag.get_text(strip=True) if title_tag else 'No title'
        date = date_tag.get_text(strip=True) if date_tag else 'No date'
        print(f"Date: {date}, Title: {title}")
    print("\n")
    time.sleep(2)


def fetch_mediatek():
    url = "https://corp.mediatek.com/news-events/press-releases"
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article', class_='entry-content block')

    print("MediaTek Press Releases:")
    for article in articles[:3]:
        title_tag = article.find('h3')
        date_tag = article.find('span', class_='date')
        title = title_tag.get_text(strip=True) if title_tag else 'No title'
        date = date_tag.get_text(strip=True) if date_tag else 'No date'
        print(f'Title: {title}')
        print(f'Date: {date}')
    print("\n")
    time.sleep(2)


def fetch_microchip():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.microchip.com/en-us/about/news-releases")

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    entries = []

    for row in soup.find_all('tr', role='row')[:3]:
        try:
            title_tag = row.find('td', class_='title-column dont_sort').find('a')
            date_tag = row.find_all('td')[1]
            title = title_tag.get_text(strip=True) if title_tag else 'No title'
            date = date_tag.get_text(strip=True) if date_tag else 'No date'
            entries.append((title, date))
        except (AttributeError, IndexError):
            continue

    print("Microchip News Releases:")
    for title, date in entries:
        print(f"Title: {title}\nDate: {date}\n")
    print("\n")
    driver.quit()
    time.sleep(2)


def fetch_minixforum():
    response = requests.get("https://theminixforum.com/index.php?forums/news-announcements.2/")
    soup = BeautifulSoup(response.content, 'html.parser')
    struct_items = soup.find_all('div', class_='structItem')

    print("Minix Forum News:")
    for item in struct_items[:3]:
        title_tag = item.find('div', class_='structItem-title').find('a')
        title = title_tag.text.strip() if title_tag else 'No title'
        date_tag = item.find('li', class_='structItem-startDate').find('time')
        date = date_tag['datetime'] if date_tag else 'No date'
        print(f"Title: {title}, Date: {date}")
    print("\n")
    time.sleep(2)


def fetch_myirtech():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get("https://www.myirtech.com/news.asp", headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr')

    print("MYIR Tech News:")
    for row in rows[:3]:
        title_tag = row.find('a', title=True)
        date_tag = row.find('td', width="10%")
        if title_tag and date_tag:
            title = title_tag.get('title', '').strip()
            date = date_tag.get_text(strip=True)
            print(f"Title: {title}, Date: {date}")
    print("\n")
    time.sleep(2)


def fetch_nxp():
    response = requests.get("https://www.nxp.com/company/about-nxp/newsroom:NEWSROOM")
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='card1-item')

    print("NXP News:")
    for entry in entries[:3]:
        title = entry.find('h3', class_='card1-title').text.strip() if entry.find('h3') else 'No title'
        date = entry.find('p', class_='metadata').text.strip() if entry.find('p') else 'No date'
        print(f"Title: {title}\nDate: {date}\n")
    print("\n")
    time.sleep(2)


def fetch_norvi():
    response = requests.get("https://norvi.lk/blog/")
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    print("NORVI Blog:")
    for article in articles[:3]:
        title_tag = article.find('h3', class_='elementor-post__title').find('a')
        date_tag = article.find('span', class_='elementor-post-date')
        title = title_tag.get_text(strip=True) if title_tag else 'No title'
        date = date_tag.get_text(strip=True) if date_tag else 'No date'
        print(f"Title: {title}, Date: {date}")
    print("\n")
    time.sleep(2)


def fetch_olimex():
    # For News
    response = requests.get("https://www.olimex.com/")
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='news')

    print("Olimex News:")
    for index, entry in enumerate(entries[:3], start=1):
        title_tag = entry.find('h2')
        date_tag = entry.find('div', class_='details').find('b')
        title = title_tag.get_text(strip=True) if title_tag else 'No title'
        date = date_tag.get_text(strip=True) if date_tag else 'No date'
        print(f"{index}. Title: {title}")
        print(f"   Date: {date}\n")

    # For Products
    response1 = requests.get("https://www.olimex.com/Products/")
    soup = BeautifulSoup(response1.content, 'html.parser')
    entries = soup.find_all('div', class_='pricing left')

    print("Olimex Products:")
    for index, entry in enumerate(entries[:3], start=1):
        title_tag = entry.find('p')
        price_tag = entry.find('div', class_='pricing default')
        title = title_tag.get_text(strip=True) if title_tag else 'No title'
        price = price_tag.get_text(strip=True) if price_tag else 'Price not found'
        print(f"{index}. Title: {title}")
        print(f"   Price: {price}\n")
    print("\n")
    time.sleep(2)


def fetch_onsemi():
    response = requests.get("https://www.onsemi.com/company/news-media/in-the-news")
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='card')

    print("Onsemi News:")
    for entry in entries[:3]:
        date_tag = entry.find('p').find('span')
        title_tag = entry.find('h6').find('a')
        date = date_tag.text if date_tag else 'No date'
        title = title_tag.text if title_tag else 'No title'
        print(f"Title: {title}\nDate: {date}\n")
    print("\n")
    time.sleep(2)


def fetch_orbbec():
    url = "https://shop.orbbec3d.com/shop"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_='facets-items-collection-view-cell-span3')

    print("Orbbec Products:")
    for item in items[:3]:
        title_element = item.find('span', itemprop='name')
        price_element = item.find('span', class_='product-views-price-lead')
        title = title_element.text.strip() if title_element else "Title not found"
        price = price_element.text.strip() if price_element else "Price not found"
        print(f"Title: {title}")
        print(f"Price: {price}\n")
    print("\n")
    time.sleep(2)
    
def fetch_picmg():
    print("Fetching PICMG Newsletter Archive...\n")
    url = "https://www.picmg.org/newsletter-archive/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://www.google.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.select('.entry-content p')

    for entry in entries[:3]:
        a_tag = entry.find('a')
        if a_tag:
            title_date = a_tag.text
            if ' – ' in title_date:
                title, date = title_date.split(' – ', 1)
            else:
                title, date = title_date, 'No date found'
            print(f"Title: {title}\nDate: {date}\n")
        else:
            print("No <a> tag found in this entry.\n")
            time.sleep(2)

def fetch_portwell():
    print("Fetching Portwell Product News...\n")
    url = "https://portwell.com/productnews.php"
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr')

    for row in rows[:3]:
        title_tag = row.find('a', class_='pr-title')
        title = title_tag.text.strip() if title_tag else 'No title found'
        date_tag = row.find('small')
        date = date_tag.text.strip() if date_tag else 'No date found'
        print(f"Title: {title}\nDate: {date}\n")
        time.sleep(2)

def fetch_qualcomm():
    print("Fetching Qualcomm News Releases...\n")
    driver = webdriver.Chrome()
    url = "https://www.qualcomm.com/news/releases"
    driver.get(url)
    time.sleep(5)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    cards = soup.find_all('div', class_='VerticalBlogCard_container__2fwPS')

    for card in cards[:3]:
        title_tag = card.find('a', class_='VerticalBlogCard_title__GUcB5')
        title = title_tag.get_text(strip=True) if title_tag else "No Title"
        date_tag = card.find('div', class_='VerticalBlogCard_metaContainer__irnWk')
        date = date_tag.find('span').get_text(strip=True) if date_tag else "No Date"
        print(f"Title: {title}\nDate: {date}\n")
    
    driver.quit()
    time.sleep(2)

def fetch_radxa():
    print("Fetching Radxa News...\n")
    url = "https://radxa.com/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news_items = soup.select('ul.news_TIAz > li')

    for item in news_items[:3]:
        title_tag = item.select_one('div.new_t_gfEZ > h2')
        title = title_tag.text.strip() if title_tag else 'No title found'
        date_tag = item.select_one('p.time_soVr')
        date = date_tag.text.strip() if date_tag else 'No date found'
        print(f"Title: {title}\nDate: {date}\n")
        time.sleep(2)

def fetch_revolutionpi():
    print("Fetching Revolution Pi Blog...\n")
    url = "https://revolutionpi.com/en/blog/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    for article in articles[:3]:
        title_element = article.find('h2', class_='entry-title')
        title = title_element.text.strip() if title_element else 'No Title Found'
        date_element = article.find('time', class_='entry-date published')
        date = date_element['datetime'] if date_element else 'No Date Found'
        print(f"Title: {title}\nDate: {date}\n")
        time.sleep(2)

def fetch_robustel():
    print("Fetching Robustel News...\n")
    url = "https://www.robustel.com/category/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='list-item')

    for entry in entries[:3]:
        title = entry.find('h1', class_='list-item-title').a.text.strip()
        print(f"Title: {title}\n")
        time.sleep(2)

def fetch_sdcard():
    print("Fetching SD Card News...\n")
    url = "https://www.sdcard.org/press/whatsnew/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for li in soup.find_all('li')[:3]:
        date_tag = li.find('time', class_='updated entry-time')
        if date_tag:
            date = date_tag.get('datetime', '').strip()
            title_tag = li.find('span', class_='bold')
            title = title_tag.a.text.strip() if title_tag and title_tag.a else title_tag.text.strip() if title_tag else ''
            print(f"Date: {date}\nTitle: {title}\n")
            time.sleep(2)

def fetch_stm():
    print("Fetching STMicroelectronics News...\n")
    url = "https://newsroom.st.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('a', class_='swiper-slide stn-card stn-card--mobile-list')

    for entry in entries[:3]:
        title_tag = entry.find('h3')
        date_tag = entry.find('div', class_='stn-card__date')
        title = title_tag.get_text(strip=True) if title_tag else 'No Title'
        date = date_tag.get_text(strip=True) if date_tag else 'No Date'
        print(f"Title: {title}\nDate: {date}\n")
        time.sleep(2)

def fetch_samsung():
    print("Fetching Samsung News...\n")
    url = "https://news.samsung.com/global/latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find('ul', class_='item').find_all('li')

    for entry in entries[:3]:
        title = entry.find('span', class_='title').text.strip()
        date = entry.find('span', class_='date').text.strip()
        print(f"Title: {title}\nDate: {date}\n")
        time.sleep(2)
        
def scrape_reolink_blog():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    response = requests.get("https://reolink.com/blog/category/news/", headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='wXzZUXnMGtTud3SFxLJy')
        print(f"Number of articles found on Reolink: {len(articles)}")
        entries = []
        
        for article in articles[:3]:
            title_tag = article.find('p', class_='xEzQ_N4GjtoQnoV_M9Bv').find('a') if article.find('p', class_='xEzQ_N4GjtoQnoV_M9Bv') else None
            date_tag = article.find('p', class_='TWnkX91XGjrLqaDYn59f')
            
            if title_tag and date_tag:
                title = title_tag.get_text(strip=True)
                date = date_tag.get_text(strip=True)
                entries.append((title, date))
        
        for index, (title, date) in enumerate(entries, start=1):
            print(f"Reolink Entry {index}:")
            print(f"Title: {title}")
            print(f"Date: {date}\n")
    else:
        print(f"Failed to retrieve the Reolink webpage. Status code: {response.status_code}")
        time.sleep(2)

# Main function to run all fetch functions
def main():
    # Fetch data from all sources
    fetch_m5stack()
    fetch_makerfabs()
    fetch_mediatek()
    fetch_microchip()
    fetch_minixforum()
    fetch_myirtech()
    fetch_nxp()
    fetch_norvi()
    fetch_olimex()
    fetch_onsemi()
    fetch_orbbec()
    fetch_picmg()
    fetch_portwell()   
    fetch_qualcomm()   
    fetch_radxa()   
    fetch_revolutionpi()   
    fetch_robustel()    
    fetch_sdcard()    
    fetch_stm()    
    fetch_samsung()    
    scrape_reolink_blog()

if __name__ == "__main__":
    main()
