import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from googletrans import Translator

# Retry settings
MAX_RETRIES = 5
RETRY_DELAY = 5  # seconds

# Utility function to check internet connection
def is_connected():
    try:
        requests.get('https://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Utility function for retry logic
def retry_request(url, headers=None, retries=MAX_RETRIES):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1}/{retries} failed: {e}")
            time.sleep(RETRY_DELAY)
            if attempt == retries - 1:
                print("Max retries reached. Exiting.")
                return None

def scrape_requests_bs4(url, headers=None):
    response = retry_request(url, headers)
    if response:
        return BeautifulSoup(response.content, 'html.parser')
    return None

def scrape_selenium_bs4(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup
    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")
        return None
    finally:
        driver.quit()

def scrape_arducam_blog():
    url = "https://www.arducam.com/blog/"
    soup = scrape_requests_bs4(url)
    if soup:
        articles = soup.find_all('article')
        for article in articles[:3]:
            title = article.find('h2', class_='entry-title').text.strip()
            date = article.find('span', class_='published').text.strip()
            print(f"Arducam Blog - Title: {title}, Date: {date}\n")

def scrape_ambarella_news():
    url = "https://www.ambarella.com/news-events/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    soup = scrape_requests_bs4(url, headers)
    if soup:
        articles = soup.find_all('article', class_='news')
        for article in articles[:3]:
            title = article.find('h2', class_='news-title').text.strip()
            date = article.find('time', class_='news-published')['datetime']
            print(f"Ambarella News - Title: {title}, Date: {date}\n")

def scrape_android_developer_news():
    url = "https://developer.android.com/news"
    soup = scrape_selenium_bs4(url)
    if soup:
        entries = soup.find_all('div', class_='devsite-card-wrapper')
        for entry in entries[:3]:
            title = entry.get('displaytitle', 'No title found')
            date = entry.find('p', class_='devsite-card-date').text.strip() if entry.find('p', class_='devsite-card-date') else 'No date found'
            print(f"Android Developer News - Title: {title}, Date: {date}\n")

def scrape_semtech_news():
    url = "https://www.semtech.com/company/news-and-media"
    soup = scrape_requests_bs4(url)
    if soup:
        cards = soup.find_all('div', class_='col-12 col-md-4 col-match-height')
        for card in cards[:3]:
            title = card.find('p', class_='h5 text-green pt-2 text-start').find('a').text.strip() if card.find('p', class_='h5 text-green pt-2 text-start').find('a') else 'No title found'
            date = card.find('span', class_='entry-meta').text.strip() if card.find('span', class_='entry-meta') else 'No date found'
            print(f"Semtech News - Title: {title}, Date: {date}\n")

def scrape_u_blox_news():
    url = "https://www.u-blox.com/en/newsroom"
    soup = scrape_selenium_bs4(url)
    if soup:
        titles = soup.find_all('a', class_='intLink w-full > h2.text-3xl')
        for title in titles[:3]:
            print(f"u-blox News - Title: {title.text.strip()}\n")

def scrape_8_devices_news():
    url = "https://www.8devices.com/news"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    soup = scrape_requests_bs4(url, headers)
    if soup:
        sections = soup.find_all('section', class_='single-post container')
        for section in sections[:3]:
            title = section.find('h3', class_='title').text.strip() if section.find('h3', class_='title') else 'No title found'
            print(f"8 Devices News - Title: {title}\n")

def scrape_aaeon_news():
    url = "https://www.aaeon.com/en/nc/product-news/"
    soup = scrape_requests_bs4(url)
    if soup:
        entries = soup.find_all('div', class_='cf iLB')
        for entry in entries[:3]:
            title = entry.find('h3').text.strip() if entry.find('h3') else 'No title found'
            date = entry.find('span', class_='date').text.strip() if entry.find('span', class_='date') else 'No date found'
            print(f"AAEON News - Title: {title}, Date: {date}\n")

def scrape_adata_news():
    url = "https://www.adata.com/in/news/"
    soup = scrape_selenium_bs4(url)
    if soup:
        news_items = soup.select('.style_card-frame__On5UP')
        for item in news_items[:3]:
            title = item.select_one('.style_card-title__Elqfd').text.strip() if item.select_one('.style_card-title__Elqfd') else 'No title found'
            day = item.select_one('.style_card-date-frame__1XNWi').text.strip() if item.select_one('.style_card-date-frame__1XNWi') else 'No day found'
            month = item.select_one('.style_card-date-year__4VAtT p:nth-of-type(2)').text.strip() if item.select_one('.style_card-date-year__4VAtT p:nth-of-type(2)') else 'No month found'
            year = item.select_one('.style_card-date-year__4VAtT p:nth-of-type(1)').text.strip() if item.select_one('.style_card-date-year__4VAtT p:nth-of-type(1)') else 'No year found'
            date = f'{day} {month} {year}'
            print(f"ADATA News - Title: {title}, Date: {date}\n")

def scrape_adlinktech_news():
    url = "https://www.adlinktech.com/en/news"
    soup = scrape_selenium_bs4(url)
    if soup:
        news_entries = soup.find_all('a', class_='latest-news')
        for entry in news_entries[:3]:
            title = entry.find('h3', class_='news-header-3').get_text(strip=True) if entry.find('h3', class_='news-header-3') else 'No title found'
            date = entry.find('p', class_='sub-info-date').get_text(strip=True) if entry.find('p', class_='sub-info-date') else 'No date found'
            print(f"ADLINK News - Title: {title}, Date: {date}\n")

def scrape_arterychip_news():
    url = "https://www.arterychip.com/en/news/index.jsp"
    soup = scrape_requests_bs4(url)
    translator = Translator()
    if soup:
        # Get all items
        items = soup.find_all('div', class_='row blog-item')
        # Iterate over the first 3 items
        for item in items[:3]:
            title = item.find('h3', class_='post-title pt1').text.strip()
            date = item.find('span', class_='date').text.strip()
            try:
                translated_title = translator.translate(title, src='auto', dest='en').text
            except Exception as e:
                translated_title = title  # Fallback to original title if translation fails
                print(f"Translation error for '{title}': {e}")
            print(f"Arterychip News - Title: {translated_title}, Date: {date}\n")


def scrape_atreyo_news():
    url = "https://atreyo.in/index.php/en/resources/blog"
    soup = scrape_requests_bs4(url)
    if soup:
        entries = [item.find('h4', class_='blog-title-views').find('span').get_text(strip=True) for item in soup.find_all('li', class_='grid')]
        for title in entries[:3]:
            print(f"Atreyo News - Title: {title}\n")

def scrape_avnet_news():
    url = "https://news.avnet.com/overview/default.aspx"
    soup = scrape_selenium_bs4(url)
    if soup:
        module_items = soup.find_all('div', class_='module_item')
        for item in module_items[:3]:
            headline_div = item.find('div', class_='module_headline')
            date_span = item.find('span', class_='module_date')
            title = headline_div.get_text(strip=True) if headline_div else 'No title found'
            date = date_span.get_text(strip=True) if date_span else 'No date found'
            print(f"Avnet News - Title: {title}, Date: {date}\n")
# Function to scrape Ahlendorf News
def scrape_ahlendorf_news():
    url = "https://ahlendorf-news.com/en/overview/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = []
    for article in soup.find_all('article')[:3]:
        title = article.find('h4', class_='media-heading').text.strip()
        date = article.find('div', class_='media-body').find_all('p')[-1].text.strip().split(',')[-1].strip()
        entries.append({'title': title, 'date': date})
    return entries

# Function to scrape Arduino Blog
def scrape_arduino_blog():
    url = "https://blog.arduino.cc/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article', class_='post')
    entries = [{'title': article.find('h2', itemprop='name headline').text.strip()} for article in articles[:3]]
    return entries

# Function to scrape ARM Newsroom
def scrape_arm_newsroom():
    url = "https://newsroom.arm.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    cards = soup.find_all('ads-card')[:3]
    entries = [{'title': card.find('h3', class_='PostAnnounce__title').get_text(strip=True),
                'date': card.find('ads-breadcrumb', class_='PostAnnounce__date').get_text(strip=True)} for card in cards[:3]]
    return entries

# Function to scrape BCM News
def scrape_bcm_news():
    url = "https://www.bcmcom.com/bcm_enewsLetter.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Send a GET request with custom headers
    response = requests.get(url, headers=headers)

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the first 3 news entries
    entries = []
    for entry in soup.find_all('div', class_='row g-mx-5--sm g-mb-30')[:3]:
        title = entry.find('h2').text.strip()
        date = entry.find('p').text.strip()
        entries.append({'title': title, 'date': date})

    return entries

# Function to scrape BeagleBoard Blog
def scrape_beagleboard_blog():
    url = "https://www.beagleboard.org/blog/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = [{'title': entry.find('p', class_='card-title').text.strip() if entry.find('p', class_='card-title') else "No title found"}
               for entry in soup.find_all('div', class_='feature-card')[:3]]
    return entries

# Function to scrape Bluetooth Events
def scrape_bluetooth_events():
    url = "https://www.bluetooth.com/events/"
    headers = {"User-Agent": "Your User-Agent String", "Referer": "https://www.yourwebsite.com", "Accept-Language": "en-US,en;q=0.9"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = [{'title': article.find('h4', class_='card-title').text.strip() if article.find('h4', class_='card-title') else "No title found",
                'date': article.find('li', class_='date').text.strip() if article.find('li', class_='date') else "No date found"}
               for article in soup.find_all('article')[:3]]
    return entries

# Function to scrape BusinessWire News
def scrape_businesswire_news():
    url = "https://www.businesswire.com/portal/site/home/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = [{'title': item.find('span', itemprop='headline').get_text(strip=True),
                'date': item.find('time', itemprop='dateModified').get_text(strip=True)}
               for item in soup.find_all('li')[:3]
               if item.find('span', itemprop='headline') and item.find('time', itemprop='dateModified')]
    return entries

# Function to scrape Collabora Blog
def scrape_collabora_blog():
    url = "https://www.collabora.com/news-and-blog/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = [{'title': entry.find('h3').find('a').get_text(strip=True), 'date': entry.find('p', class_='_2016datestamp').find('strong').get_text(strip=True)}
               for entry in soup.find_all('div', class_='BlogAndNewsArticleTplWrapper')[:3]]
    return entries

# Function to scrape Coral AI News
def scrape_coral_ai_news():
    url = "https://coral.ai/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = []
    for article in soup.find_all('article', class_='home-tile')[:3]:
        title_tag = article.find('h2', class_='home-external-tile__header__big-title')
        date_tag = article.find('span', class_='home-external-tile__content__date')
        if title_tag and date_tag:
            title = title_tag.text.strip()
            date = date_tag.text.strip()
            entries.append({'title': title, 'date': date})
    return entries

# Function to scrape CTL Insights Blog
def scrape_ctl_insights_blog():
    url = "https://ctl.net/blogs/insights"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = [{'title': item.find('h3', class_='article-item__title').get_text(strip=True),
                 'date': item.find('time', class_='article__meta-item article__date').get_text(strip=True)}
                for item in soup.find_all('div', class_='article-item')[:3]]
    return articles

# Function to scrape Cytron News
def scrape_cytron_news():
    url = "https://www.cytron.io/tutorial/miscellaneous/news"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = []
    blog_items = soup.find_all('div', class_='blog-grid-item')
    for item in blog_items[:3]:
        title_tag = item.find('h3').find('a')
        title = title_tag.text.strip() if title_tag else 'No title found'
        author_tag = item.find('div', class_='author').find('a')
        date_author_text = author_tag.text.strip() if author_tag else 'No date found'
        date = date_author_text.split(',')[-1].strip() if ',' in date_author_text else 'No date found'
        entries.append((title, date))
    return entries

def parse_dfi_pressroom():
    url = "https://www.dfi.com/pressroom?news=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('a', class_='item')

    results = []
    for entry in entries[:3]:
        title_element = entry.find('h3', class_='title')
        title = title_element.text.strip() if title_element else 'No Title Found'
        date_element = entry.find('div', class_='date')
        date = date_element.text.strip() if date_element else 'No Date Found'
        results.append({'title': title, 'date': date})

    return results

def parse_dfrobot_blog():
    url = "https://www.dfrobot.com/blog"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = [title.text for title in soup.find_all('a', class_='title')]
    return titles[:3]

def parse_digi_press_releases():
    url = "https://www.digi.com/company/press-releases"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='item')

    results = []
    for entry in entries[:3]:
        title = entry.find('h3').text.strip()
        date = entry.find('span', class_='date').text.strip()
        results.append({'title': title, 'date': date})
    return results

def parse_dusuniot_news():
    url = "https://www.dusuniot.com/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = []
    for article in soup.find_all('article', class_='elementor-post'):
        title_tag = article.find('h3', class_='elementor-post__title')
        if title_tag and title_tag.a:
            titles.append(title_tag.a.text.strip())
    return titles[:3]

def parse_ecsipc_news():
    url = "https://www.ecsipc.com/en/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='item')

    results = []
    for entry in entries[:3]:
        date_tag = entry.find('div', class_='tag-date').find('span', class_='name')
        date = date_tag.get_text(strip=True) if date_tag else 'No date'
        title_tag = entry.find('h4').find('a', class_='title')
        title = title_tag.get_text(strip=True) if title_tag else 'No title'
        results.append({'title': title, 'date': date})
    return results

def parse_edatec_products():
    url = "https://www.edatec.cn/en/product/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.select('.blog-article')

    results = []
    for article in articles[:3]:
        title = article.select_one('.entry-title a').text.strip()
        date = article.select_one('.entry-date time').get('datetime').strip()
        results.append({'title': title, 'date': date})
    return results

def parse_edgeimpulse_blog():
    url = "https://edgeimpulse.com/blog/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('article', class_='flex')

    results = []
    for entry in entries[:3]:
        title = entry.find('h3').text.strip()
        time_tag = entry.find('time')
        date = time_tag['datetime'] if time_tag and 'datetime' in time_tag.attrs else 'No Date Found'
        results.append({'title': title, 'date': date})
    return results


def parse_efinix_news():
    url = "https://www.efinixinc.com/company-news.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('div', class_='col')

        results = []
        for entry in entries[:3]:
            title_tag = entry.find('h4')
            date_tag = entry.find('span', class_='gray')
            title = title_tag.get_text(strip=True) if title_tag else 'No Title Found'
            date = date_tag.get_text(strip=True) if date_tag else 'No Date Found'
            results.append({'title': title, 'date': date})
        return results
    else:
        return []

def parse_elecrow_news():
    url = "https://www.elecrow.com/blog/elecrow-news"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        posts = soup.find_all('li', class_='post-item')

        results = []
        for post in posts[:3]:
            title = post.find('h3', class_='post-title').get_text(strip=True)
            date = post.find('span', class_='post-date').get_text(strip=True)
            results.append({'title': title, 'date': date})
        return results
    else:
        return []

def parse_elegoo_blog():
    url = "https://www.elegoo.com/pages/blog-collection#3d"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    blog_posts = soup.find_all('div', class_='blog-post')

    results = []
    for post in blog_posts[:3]:
        title = post.find('h5').get_text(strip=True)
        date = post.find('aside', class_='post-meta').get_text(strip=True)
        results.append({'title': title, 'date': date})
    return results

def parse_emporia_news():
    url = "https://www.emporiaenergy.com/blog/?e-filter-4847f41-category=news"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', class_='elementor-element elementor-element-2d5d436c premium-header-inline elementor-widget elementor-widget-premium-addon-dual-header')

    results = []
    for article in articles[:3]:
        title_tag = article.find('h2', class_='premium-dual-header-first-header')
        title = title_tag.text.strip() if title_tag else 'No Title Found'
        date_tag = article.find('time')
        date = date_tag.text.strip() if date_tag else 'No Date Found'
        results.append({'title': title, 'date': date})
    return results

def parse_firefly_news():
    url = "https://en.t-firefly.com/news.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='news-list')

    results = []
    for entry in entries[:3]:
        title_tag = entry.find('h4').find('a')
        title = title_tag.get_text(strip=True) if title_tag else 'No title'
        date_tag = entry.find('div', class_='other').find('span')
        date = date_tag.get_text(strip=True) if date_tag else 'No date'
        results.append({'title': title, 'date': date})
    return results

def parse_friendlyelec_forum():
    url = "https://www.friendlyelec.com/Forum/viewforum.php?f=3"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr', class_='t-row clickable')

        results = []
        for row in rows[:3]:
            title_tag = row.find('a', class_='topictitle')
            title = title_tag.text.strip() if title_tag else 'No title found'
            date_tag = row.find('small')
            date = date_tag.text.strip() if date_tag else 'No date found'
            results.append({'title': title, 'date': date})
        return results
    else:
        return []

def parse_geekom_forums():
    url = "https://community.geekompc.com/forums/official-news-and-deals.38/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    threads = soup.find_all('div', class_='structItem')

    results = []
    for thread in threads[:3]:
        title_tag = thread.find('div', class_='structItem-title')
        title = title_tag.find_all('a')[-1].get_text(strip=True) if title_tag else 'No Title Found'
        date_tag = thread.find('time', class_='structItem-latestDate u-dt')
        date = date_tag.get_text(strip=True) if date_tag else 'No Date Found'
        results.append({'title': title, 'date': date})
    return results

def parse_getiot_news():
    url = "https://getiot.tech/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', class_='masonry-post')

    results = []
    for article in articles[:3]:
        title_tag = article.find('h4')
        title = title_tag.text.strip() if title_tag else 'No Title Found'
        date_tag = article.find('span', class_='date')
        date = date_tag.text.strip() if date_tag else 'No Date Found'
        results.append({'title': title, 'date': date})
    return results

def scrape_ecsipc_news():
    response = requests.get("https://www.ecsipc.com/en/news")
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='item')
    print("ECSIPC News:\n")
    for entry in entries[:3]:
        date_tag = entry.find('div', class_='tag-date').find('span', class_='name')
        date = date_tag.get_text(strip=True) if date_tag else 'No date'
        title_tag = entry.find('h4').find('a', class_='title')
        title = title_tag.get_text(strip=True) if title_tag else 'No title'
        print(f"Title: {title}")
        print(f"Date: {date}\n")
    time.sleep(2)

def scrape_glinet_blog():
    response = requests.get("https://blog.gl-inet.com/")
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='row')
    titles = []
    print("GL.iNet Blog:\n")
    for entry in entries[:3]:
        title_container = entry.find('h3', class_='post-title')
        if title_container:
            title_tag = title_container.find('a')
            title = title_tag.get_text(strip=True) if title_tag else 'No title'
            titles.append(title)
    for title in titles:
        print(f"Title: {title}\n")
    time.sleep(2)

def scrape_gigadevice_news():
    response = requests.get("https://www.gigadevice.com/about/news-and-event/news")
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='he_h2p2hul clearfix')
    print("GigaDevice News:\n")
    for entry in entries[:3]:
        articles = entry.find_all('div', class_='he_h2p2hli fl')
        for article in articles[:3]:
            date = article.find('div', class_='he_h2p2htim').p.text.strip()
            title = article.find('div', class_='he_h2p2hxp').p.text.strip()
            print(f"Date: {date}")
            print(f"Title: {title}\n")
    time.sleep(2)

def scrape_gettobyte_blogs():
    response = requests.get("https://gettobyte.in/semiconductor-chip-blogs/")
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='serv-box-2 s2')
    print("Gettobyte Blogs:\n")
    for entry in entries[:3]:
        title = entry.find('h5').text.strip()
        print(f"Entry Title: {title}\n")
    time.sleep(2)

def scrape_hubitat_press_releases():
    response = requests.get("https://hubitat.com/pages/press-releases")
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='press-releases press__grid')
    print("Hubitat Press Releases:\n")
    for entry in entries[:3]:
        paragraphs = entry.find_all('p')
        for paragraph in paragraphs:
            date = paragraph.find('span').text.strip() if paragraph.find('span') else ''
            title = paragraph.find('a').text.strip() if paragraph.find('a') else ''
            print(f"Title: {title}")
            print(f"Date: {date}\n")
    time.sleep(2)

def scrape_industrial_shields_blog():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    url = "https://www.industrialshields.com/blog/arduino-raspberry-pi-industrial-news-industry-4-0-iot-11"
    driver.get(url)
    time.sleep(10)
    html_content = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = soup.find_all('article', class_='o_wblog_post')
    titles = []
    print("Industrial Shields Blog:\n")
    for article in articles[:3]:
        title_tag = article.find('a', class_='o_blog_post_title')
        if title_tag:
            title = title_tag.text.strip()
            titles.append(title)
    for title in titles:
        print(title)
    time.sleep(2)

def scrape_inventia_news():
    options = Options()
    options.headless = True
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://inventia.online/news/")
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    titles = []
    print("Inventia News:\n")
    for h4 in soup.find_all('h4'):
        a_tag = h4.find('a')
        if a_tag:
            titles.append(a_tag.get_text())
    if titles:
        for title in titles[:3]:
            print(title)
    else:
        print("No titles found")
    driver.quit()
    time.sleep(2)

def scrape_jetway_news():
    response = requests.get("https://jetwayipc.com/jetwaynews/?lang=en")
    soup = BeautifulSoup(response.content, 'html.parser')
    post_items = soup.find_all('div', class_='post-item')
    print("Jetway News:\n")
    titles = []
    for item in post_items[:3]:
        title = item.find('h5', class_='post-title').text.strip()
        titles.append(title)
    for title in titles:
        print(f"Title: {title}\n")
    time.sleep(2)

def scrape_lenovo_press_releases():
    response = requests.get("https://news.lenovo.com/pressroom/press-releases/")
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='card card-wide card-release')
    print("Lenovo Press Releases:\n")
    for entry in entries[:3]:
        date = entry.find('small', class_='card-date card-list-date').text.strip()
        title = entry.find('h3', class_='card-title card-list-title').a.text.strip()
        print(f"Title: {title}")
        print(f"Date: {date}\n")
    time.sleep(2)

def scrape_luckfox_products():
    response = requests.get("https://www.luckfox.com/index.php?route=product/catalog")
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('div', class_='name').a.get_text(strip=True)
    price = soup.find('span', class_='price-normal').get_text(strip=True)
    print("LuckFox Products:\n")
    print(f"Title: {title}")
    print(f"Price: {price}\n")
    time.sleep(2)

def main():
    # Check internet connection before starting the scraping process
    while not is_connected():
        print("Internet connection not available. Retrying...")
        time.sleep(RETRY_DELAY)
        
    print("Scraping Arducam Blog:")
    scrape_arducam_blog()
    print("\nScraping Ambarella News:")
    scrape_ambarella_news()
    print("\nScraping Android Developer News:")
    scrape_android_developer_news()
    print("\nScraping Semtech News:")
    scrape_semtech_news()
    print("\nScraping u-blox News:")
    scrape_u_blox_news()
    print("\nScraping 8 Devices News:")
    scrape_8_devices_news()
    print("\nScraping AAEON News:")
    scrape_aaeon_news()
    print("\nScraping ADATA News:")
    scrape_adata_news()
    print("\nScraping ADLINK News:")
    scrape_adlinktech_news()
    print("\nScraping Arterychip News:")
    scrape_arterychip_news()
    print("\nScraping Atreyo News:")
    scrape_atreyo_news()
    print("\nScraping Avnet News:")
    scrape_avnet_news()
    print("Ahlendorf News:")
    for entry in scrape_ahlendorf_news():
        print(f"Title: {entry['title']}\nDate: {entry['date']}\n")

    print("Arduino Blog:")
    for entry in scrape_arduino_blog():
        print(f"Title: {entry['title']}\n")

    print("ARM Newsroom:")
    for entry in scrape_arm_newsroom():
        print(f"Title: {entry['title']}\nDate: {entry['date']}\n")

    print("BCM News:")
    for entry in scrape_bcm_news():
        print(f"Title: {entry['title']}\nDate: {entry['date']}\n")

    print("BeagleBoard Blog:")
    for entry in scrape_beagleboard_blog():
        print(f"Title: {entry['title']}\n")

    print("Bluetooth Events:")
    for entry in scrape_bluetooth_events():
        print(f"Title: {entry['title']}\nDate: {entry['date']}\n")

    print("BusinessWire News:")
    for entry in scrape_businesswire_news():
        print(f"Title: {entry['title']}, Date: {entry['date']}\n")

    print("Collabora Blog:")
    for entry in scrape_collabora_blog():
        print(f"Title: {entry['title']}, Date: {entry['date']}\n")

    print("Coral AI News:")
    for entry in scrape_coral_ai_news():
        print(f"Entry Title: {entry['title']}\nDate: {entry['date']}\n")

    print("CTL Insights Blog:")
    for entry in scrape_ctl_insights_blog():
        print(f"Title: {entry['title']}\nDate: {entry['date']}\n")

    print("Cytron News:")
    for entry in scrape_cytron_news():
        print(f"Title: {entry[0]}\nDate: {entry[1]}\n")
        
    all_results = {
        "DFI Pressroom": parse_dfi_pressroom(),
        "DFRobot Blog": parse_dfrobot_blog(),
        "Digi Press Releases": parse_digi_press_releases(),
        "DusunIoT News": parse_dusuniot_news(),
        "ECSIPC News": parse_ecsipc_news(),
        "Edatec Products": parse_edatec_products(),
        "EdgeImpulse Blog": parse_edgeimpulse_blog(),
        "Efinix News": parse_efinix_news(),
        "Elecrow News": parse_elecrow_news(),
        "Elegoo Blog": parse_elegoo_blog(),
        "Emporia News": parse_emporia_news(),
        "Firefly News": parse_firefly_news(),
        "FriendlyELEC Forum": parse_friendlyelec_forum(),
        "GEEKOM Forums": parse_geekom_forums(),
        "GetIoT News": parse_getiot_news()
    }

    for site, results in all_results.items():
        print(f"\nResults from {site}:")
        for result in results:
            print(result)
        time.sleep(2)
        
    scrape_ecsipc_news()
    scrape_glinet_blog()
    scrape_gigadevice_news()
    scrape_gettobyte_blogs()
    scrape_hubitat_press_releases()
    scrape_industrial_shields_blog()
    scrape_inventia_news()
    scrape_jetway_news()
    scrape_lenovo_press_releases()
    scrape_luckfox_products()

if __name__ == "__main__":
    main()
