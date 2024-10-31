import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from googletrans import Translator
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager


# Set up the Selenium WebDriver with Chrome in headless mode
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

firefox_options = FirefoxOptions()
firefox_options.headless = True

# Initialize WebDriver
chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


# List of URLs to scrape
chrome_urls = [
    "https://developer.android.com/news",
    "https://www.u-blox.com/en/newsroom",
    "https://www.adata.com/in/news/",
    "https://www.adlinktech.com/en/news",
    "https://news.avnet.com/overview/default.aspx",
    "https://www.emporiaenergy.com/blog/?e-filter-4847f41-category=news",
    "https://www.industrialshields.com/blog/arduino-raspberry-pi-industrial-news-industry-4-0-iot-11",
    "https://inventia.online/news/",
    "https://www.qualcomm.com/news/releases",
    "https://www.seco.com/news",
    "https://www.solid-run.com/press-room/",
    "https://wiki.sipeed.com/news/",
    "https://www.waveshare.com/new?dir=desc&order=position",
    "https://www.asrockind.com/en-gb/article-category/19",
    "https://discuss.luxonis.com/blog",
    "https://www.nordicsemi.com/Nordic-news",
    "https://www.renesas.com/us/en/about/newsroom#latest-press-releases"
]

# URL to scrape with Firefox (microchip.com)
firefox_url = "https://www.microchip.com/en-us/about/news-releases"

# Initialize an empty list to hold all the scraped data
data = []

# Translator for translating text if necessary
translator = Translator()

# Function to scrape each site and print the extracted titles and dates
def scrape_with_chrome(url):
    company_name = url.split("/")[2]  # Extracting the domain name as company name
    print(f"Scraping {url}...")
    chrome_driver.get(url)
    time.sleep(10)  # Allow time for page load

    soup = BeautifulSoup(chrome_driver.page_source, 'html.parser')


    # Site-specific parsing based on structure
    if "developer.android.com" in url:
        entries = soup.find_all('div', class_='devsite-card-wrapper')
        for entry in entries[:3]:
            title = entry.get('displaytitle', 'No title found')
            date = 'No date found'  # Adjust if there's a date to extract
            data.append([company_name, title, date])
            print(f"Company: {company_name}, Title: {title}, Date: {date}")
            time.sleep(2)

    elif "u-blox.com" in url:
        titles = chrome_driver.find_elements(By.CSS_SELECTOR, 'a.intLink.w-full > h2.text-3xl')
        for title in titles[:3]:
            data.append([company_name, title.text.strip(), 'No date found'])
            print(f"Company: {company_name}, Title: {title.text.strip()}, Date: No date found")
            time.sleep(2)

    elif "adata.com" in url:
        entries = soup.select('.style_card-frame__On5UP')
        for item in entries[:3]:
            title = item.select_one('.style_card-title__Elqfd').text.strip() if item.select_one(
                '.style_card-title__Elqfd') else 'No title found'
            day = item.select_one('.style_card-date-frame__1XNWi').text.strip() if item.select_one(
                '.style_card-date-frame__1XNWi') else 'No day found'
            month = item.select_one('.style_card-date-year__4VAtT p:nth-of-type(2)').text.strip() if item.select_one(
                '.style_card-date-year__4VAtT p:nth-of-type(2)') else 'No month found'
            year = item.select_one('.style_card-date-year__4VAtT p:nth-of-type(1)').text.strip() if item.select_one(
                '.style_card-date-year__4VAtT p:nth-of-type(1)') else 'No year found'
            date = f'{day} {month} {year}'
            data.append([company_name, title, date])
            print(f"Company: {company_name}, Title: {title}, Date: {date}")
            time.sleep(2)



    elif "adlinktech.com" in url:

        news_entries = soup.find_all('a', class_='latest-news')

        for entry in news_entries[:3]:
            title = entry.find('h3', class_='news-header-3').get_text(strip=True) if entry.find('h3',
                                                                                                class_='news-header-3') else 'No title found'

            date = entry.find('p', class_='sub-info-date').get_text(strip=True) if entry.find('p',
                                                                                              class_='sub-info-date') else 'No date found'

            data.append([company_name, title, date])

            print(f"Company: {company_name}, Title: {title}, Date: {date}")
            time.sleep(2)

    if "news.avnet.com" in url:
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "module_item"))
        )
        module_items = soup.find_all('div', class_='module_item')
        for item in module_items[:3]:
            title = item.find('div', class_='module_headline').get_text(strip=True) if item.find('div',
                                                                                                 class_='module_headline') else 'No title found'
            date = item.find('span', class_='module_date-text').get_text(strip=True) if item.find('span',
                                                                                                  class_='module_date-text') else 'No date found'
            data.append([company_name, title, date])
            print(f"Company: {company_name}, Title: {title}, Date: {date}")
            time.sleep(2)

    elif "emporiaenergy.com" in url:
        articles = soup.find_all('div',
                                 class_='elementor-element elementor-element-2d5d436c premium-header-inline elementor-widget elementor-widget-premium-addon-dual-header')
        for article in articles[:3]:
            title = article.find('h2', class_='premium-dual-header-first-header').text.strip() if article.find('h2',
                                                                                                               class_='premium-dual-header-first-header') else 'No Title Found'
            date = article.find('time').text.strip() if article.find('time') else 'No Date Found'
            data.append([company_name, title, date])
            print(f"Company: {company_name}, Title: {title}, Date: {date}")
            time.sleep(2)


    elif "industrialshields.com" in url:

        articles = soup.find_all('article', class_='o_wblog_post')

        for article in articles[:3]:
            title = article.find('a', class_='o_blog_post_title').get_text(strip=True) if article.find('a',
                                                                                                       class_='o_blog_post_title') else 'No title found'

            date = article.find('time').get_text(strip=True) if article.find('time') else 'No date found'

            data.append([company_name, title, date])

            print(f"Company: {company_name}, Title: {title}, Date: {date}")
            time.sleep(2)

    elif "inventia.online" in url:
        titles = [a.get_text() for h4 in soup.find_all('h4') for a in h4.find_all('a')]
        for title in titles[:3]:
            data.append([company_name, title, 'No Date Found'])
            print(f"Company: {company_name}, Title: {title}, Date: No Date Found")
            time.sleep(2)



    elif "qualcomm.com" in url:
        cards = soup.find_all('div', class_='VerticalBlogCard_container__2fwPS')
        for card in cards[:3]:
            title = card.find('a', class_='VerticalBlogCard_title__GUcB5').get_text(strip=True) if card.find('a',
                                                                                                             class_='VerticalBlogCard_title__GUcB5') else 'No Title Found'
            date = card.find('div', class_='VerticalBlogCard_metaContainer__irnWk').find('span').get_text(
                    strip=True) if card.find('div', class_='VerticalBlogCard_metaContainer__irnWk') and card.find('div',
                                                                                                              class_='VerticalBlogCard_metaContainer__irnWk').find(
                'span') else 'No Date Found'
            data.append([company_name, title, date])
            print(f"Company: {company_name}, Title: {title}, Date: {date}")
            time.sleep(2)



    elif "seco.com" in url:

        WebDriverWait(chrome_driver, 15).until(

            EC.presence_of_all_elements_located((By.CLASS_NAME, 'media'))

        )

        time.sleep(2)  # Extra wait to ensure all elements are fully loaded

        entries = soup.find_all('div', class_='media', limit=3)

        for entry in entries:
            title = entry.find('span', itemprop='headline').text.strip() if entry.find('span',
                                                                                       itemprop='headline') else "Title not found"

            date = entry.find('div', class_='card-text').text.strip() if entry.find('div',
                                                                                    class_='card-text') else "Date not found"

            data.append([company_name, title, date])

            print(f"Company: {company_name}, Title: {title}, Date: {date}")


    elif "solid-run.com" in url:
        headers = soup.find_all('header', class_='entry-content-header')
        for header in headers[:3]:
            date_tag = header.find('time', class_='av-magazine-time')
            date = date_tag.get_text(strip=True) if date_tag else 'No date found'
            title_tag = header.find('h3', class_='av-magazine-title')
            title = title_tag.get_text(strip=True) if title_tag else 'No title found'
            data.append([company_name, title, date])
            print(f"Company: {company_name}, Title: {title}, Date: {date}")
            time.sleep(2)

    elif "sipeed.com" in url:
        titles = [a.h2.get_text(strip=True) for a in soup.find_all('a', class_='blog_title')]
        translated_titles = [translator.translate(title, src='zh-cn', dest='en').text for title in titles[:3]]
        for title in translated_titles:
            data.append([company_name, title, 'No date provided'])
            print(f"Company: {company_name}, Title: {title}, Date: No date provided")
            time.sleep(2)



    elif "waveshare.com" in url:

    # Find product titles on the Waveshare page

        titles = [h2.a.get_text(strip=True) for h2 in soup.find_all('h2', class_='product-name')]

        for title in titles[:3]:  # Limit to 3 entries

            data.append([company_name, title, 'No date provided'])

            print(f"Company: {company_name}, Title: {title}, Date: No date provided")
            time.sleep(2)

    elif "asrockind.com" in url:
        articles = soup.find_all('div', class_='box-1 border-bottom pb-3 pt-3 pl-md-3')[:3]
        for article in articles:
            title = article.find('h4').text.strip() if article.find('h4') else 'No title found'
            date = article.find('span', class_='date').text.strip() if article.find('span',
                                                                                    class_='date') else 'No date found'
            data.append([company_name, title, date])
            print(f"Company: {company_name}, Title: {title}, Date: {date}")
            time.sleep(2)

    elif "luxonis.com" in url:
        entries = [item.find('h4').text.strip() for item in soup.find_all('a', class_='BlogList-item')[:3] if
                item.find('h4')]
        for title in entries:
            data.append([company_name, title, 'No Date Found'])
            print(f"Company: {company_name}, Title: {title}, Date: No Date Found")
            time.sleep(2)

    elif "nordicsemi.com" in url:
        news_items = soup.find_all('div', class_='news-archive-box')[:3]
        for item in news_items:
            title = item.find('div', class_='text-wrap').text.strip() if item.find('div',
                                                                                   class_='text-wrap') else 'No title found'
            date = item.find('div', class_='tag overlay').text.strip() if item.find('div',
                                                                                    class_='tag overlay') else 'No date found'
            data.append([company_name, title, date])
            print(f"Company: {company_name}, Title: {title}, Date: {date}")
            time.sleep(2)

    elif "renesas.com" in url:
        items = soup.find_all('div', class_='item-wrapper press-releases-item-wrapper')[:3]
        for item in items:
            title = item.find('div', class_='item-title press-releases-item-title').text.strip() if item.find('div',
                                                                                                              class_='item-title press-releases-item-title') else 'No title found'
            date = item.find('time', class_='datetime press-releases-datetime')['datetime'] if item.find('time',
                                                                                                         class_='datetime press-releases-datetime') else 'No date found'
            data.append([company_name, title, date])
            print(f"Company: {company_name}, Title: {title}, Date: {date}")
            time.sleep(2)

    print("\n" + "-" * 50 + "\n")


# Function to scrape Microchip site with Firefox
def scrape_microchip_with_firefox():
    company_name = "microchip.com"
    print(f"Scraping {firefox_url} with Firefox...")
    firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    firefox_driver.get(firefox_url)
    time.sleep(3)  # Allow time for page load

    soup = BeautifulSoup(firefox_driver.page_source, 'html.parser')
    entries = []

    # Find all table rows with the role attribute set to 'row'
    for row in soup.find_all('tr', role='row'):
        try:
            title_tag = row.find('td', class_='title-column dont_sort').find('a')
            date_tag = row.find_all('td')[1]

            if title_tag and date_tag:
                title = title_tag.get_text(strip=True)
                date = date_tag.get_text(strip=True)
                data.append([company_name, title, date])
                print(f"Company: {company_name}, Title: {title}, Date: {date}")
        except (AttributeError, IndexError) as e:
            continue

    firefox_driver.quit()
    print("\n" + "-" * 50 + "\n")

# Run the scraper for each URL
for url in chrome_urls:
    try:
        scrape_with_chrome(url)
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Scrape Microchip with Firefox
scrape_microchip_with_firefox()


# Close the WebDriver after all scraping is done
chrome_driver.quit()

# Convert the list to a DataFrame
df = pd.DataFrame(data, columns=['Company', 'Titles', 'Date'])

# Print data in the terminal
print(df)

# Save the data to an Excel file
df.to_excel("merge2.xlsx", index=False)
print("Data saved to 'merge2.xlsx'")
