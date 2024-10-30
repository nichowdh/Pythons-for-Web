import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


# Common headers for all requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# List to hold data
data = []

def fetch_ambarella():
    url = "https://www.ambarella.com/news-events/"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article', class_='news')
        for article in articles[:3]:
            news_title = article.find('h2', class_='news-title').text.strip()
            news_date = article.find('time', class_='news-published')['datetime']
            data.append({"Company": "Ambarella", "Title": news_title, "Date": news_date})
            print(f"Fetched Ambarella - Title: {news_title}, Date: {news_date}")  # Debug print
            time.sleep(2)
    else:
        print("Failed to fetch data")

def fetch_8devices():
    url = "https://www.8devices.com/news"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('a', class_='news-article-card')
        for article in articles[:3]:
            title_tag = article.find('h3', class_='brxe-uzsxwg brxe-heading h6')
            title = title_tag.text.strip() if title_tag else 'No title found'
            data.append({"Company": "8Devices", "Title": title, "Date": ""})
            print(f"8Devices - Title: {title}\n")
            time.sleep(2)
    else:
        print("Failed to fetch data")

def fetch_arduino():
    url = "https://blog.arduino.cc/"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article', class_='post')
        for article in articles[:3]:
            title_elem = article.find('h2', itemprop='name headline')
            title = title_elem.text.strip() if title_elem else 'Title not found'
            data.append({"Company": "Arduino Blog", "Title": title, "Date": ""})
            print(f"Arduino Blog - Title: {title}\n")
            time.sleep(2)
    else:
        print("Failed to fetch data")

def fetch_bcmcom():
    url = "https://www.bcmcom.com/bcm_enewsLetter.html"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('div', class_='row g-mx-5--sm g-mb-30')
        for entry in entries[:3]:
            date = entry.find('p').text.strip()
            title = entry.find('h2').text.strip()
            data.append({"Company": "BCMCOM", "Title": title, "Date": ""})
            print(f"BCMCOM - Title: {title}, Date: {date}\n")
            time.sleep(2)
    else:
        print("Failed to fetch data")

def fetch_bluetooth():
    url = "https://www.bluetooth.com/events/"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles[:3]:
            title_elem = article.find('h4', class_='card-title')
            date_elem = article.find('li', class_='date')
            title = title_elem.text.strip() if title_elem else "No title found"
            date = date_elem.text.strip() if date_elem else "No date found"
            data.append({"Company": "Bluetooth Events", "Title": title, "Date": ""})
            print(f"Bluetooth Events - Title: {title}, Date: {date}\n")
            time.sleep(2)
    else:
        print("Failed to fetch data")

def fetch_cytron():
    url = "https://www.cytron.io/tutorial/miscellaneous/news"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        blog_items = soup.find_all('div', class_='blog-grid-item')
        for item in blog_items[:3]:
            title_tag = item.find('h3').find('a')
            author_tag = item.find('div', class_='author').find('a')
            title = title_tag.text.strip() if title_tag else 'No title found'
            date_author_text = author_tag.text.strip() if author_tag else 'No date found'
            date = date_author_text.split(',')[-1].strip() if ',' in date_author_text else 'No date found'
            data.append({"Company": "Cytron", "Title": title, "Date": date})
            print(f"Cytron - Title: {title}, Date: {date}\n")
            time.sleep(2)
    else:
        print("Failed to fetch data")

def fetch_efinix():
    url = "https://www.efinixinc.com/company-news.html"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('div', class_='col')
        for entry in entries[:3]:
            title_tag = entry.find('h4')
            date_tag = entry.find('span', class_='gray')
            title = title_tag.get_text(strip=True) if title_tag else 'Title not found'
            date = date_tag.get_text(strip=True) if date_tag else 'Date not found'
            data.append({"Company": "Efinix", "Title": title, "Date": date})
            print(f"Efinix - Title: {title}, Date: {date}\n")
            time.sleep(2)
    else:
        print("Failed to fetch data")

def fetch_luckfox():
    url = "https://www.luckfox.com/index.php?route=product/catalog"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.select('.product-layout')
        for product in products[:3]:
            title = product.select_one('.name a').text.strip()
            price = product.select_one('.price-normal').text.strip()
            data.append({"Company": "8Devices", "Title": title, "Date": ""})
            print(f"LuckFox - Title: {title}, Price: {price}\n")
            time.sleep(2)
    else:
        print("Failed to fetch data")

def fetch_myirtech():
    url = "https://www.myirtech.com/news.asp"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr')
        entries = set()
        for row in rows[:3]:
            title_tag = row.find('a', title=True)
            date_tag = row.find('td', width="10%")
            title = title_tag.get('title', '').strip() if title_tag else "No title found"
            date = date_tag.get_text(strip=True) if date_tag else "No date found"
            entries.add((title, date))
        for title, date in entries:
            data.append({"Company": "MyirTech", "Title": title, "Date": date})
            print(f"MyirTech - Title: {title}, Date: {date}\n")
            time.sleep(2)
    else:
        print("Failed to fetch data")

def fetch_picmg():
    url = "https://www.picmg.org/newsletter-archive/"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.select('.entry-content p')
        for entry in entries[:3]:
            a_tag = entry.find('a')
            if a_tag:
                title_date = a_tag.text
                title, date = (title_date.split(' – ', 1) if ' – ' in title_date else (title_date, 'No date found'))
                data.append({"Company": "PICMG", "Title": title, "Date": date})
                print(f"PICMG - Title: {title}, Date: {date}\n")
                time.sleep(2)
    else:
        print("Failed to fetch data")

def fetch_reolink():
    url = "https://reolink.com/blog/category/news/"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='wXzZUXnMGtTud3SFxLJy')
        for article in articles[:3]:
            title_tag = article.find('p', class_='xEzQ_N4GjtoQnoV_M9Bv').find('a') if article.find('p', class_='xEzQ_N4GjtoQnoV_M9Bv') else None
            date_tag = article.find('p', class_='TWnkX91XGjrLqaDYn59f')
            title = title_tag.get_text(strip=True) if title_tag else "No title found"
            date = date_tag.get_text(strip=True) if date_tag else "No date found"
            data.append({"Company": "Reolink", "Title": title, "Date": date})
            print(f"Reolink - Title: {title}, Date: {date}\n")
            time.sleep(2)
    else:
        print("Failed to fetch data")

def fetch_revolution_pi():
    url = "https://revolutionpi.com/en/blog/"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles[:3]:
            title_elem = article.find('h2', class_='entry-title')
            date_elem = article.find('time', class_='entry-date published')
            title = title_elem.text.strip() if title_elem else "No title found"
            date = date_elem['datetime'] if date_elem else "No date found"
            data.append({"Company": "Revolution Pi", "Title": title, "Date": date})
            print(f"Revolution Pi - Title: {title}, Date: {date}\n")
            time.sleep(2)
    else:
        print("Failed to fetch data")

def fetch_mekotronics():
    url = "https://www.mekotronics.com/h-col-104.html"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = [a['title'] for a in soup.find_all('a', class_='fk-productName')]
        for title in titles[:3]:
            data.append({"Company": "8Devices", "Title": title, "Date": ""})
            print(f"Mekotronics - Title: {title}\n")
            time.sleep(2)
    else:
        print("Failed to fetch data")

# Save data to Excel
def save_to_excel(data):
    # Check if data is not empty
    if data:
        # Convert data to DataFrame
        df = pd.DataFrame(data)
        print("Data collected:", df)  # Debug print
        # Save to Excel file
        df.to_excel("output.xlsx", index=False)
        print("Data saved to output.xlsx")
    else:
        print("No data to save")

# Fetching data from all sites
fetch_ambarella()
fetch_8devices()
fetch_arduino()
fetch_bcmcom()
fetch_bluetooth()
fetch_cytron()
fetch_efinix()
fetch_luckfox()
fetch_myirtech()
fetch_picmg()
fetch_reolink()
fetch_revolution_pi()
fetch_mekotronics()

# Save data to Excel
save_to_excel(data)