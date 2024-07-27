import requests
from bs4 import BeautifulSoup
import time
import sys

# Function to check for "product page" and "press release" links in an article
def check_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    product_page_link = None
    press_release_link = None
    
    # Look for links containing "product page" and "press release"
    for a_tag in soup.find_all('a', href=True):
        if 'product page' in a_tag.get_text(strip=True).lower():
            product_page_link = a_tag['href']
        if 'press release' in a_tag.get_text(strip=True).lower():
            press_release_link = a_tag['href']
    
    return product_page_link, press_release_link

# Function to parse the main page and extract article information
def parse_main_page(page_number):
    url = f"https://www.cnx-software.com/page/{page_number}/"
    response = requests.get(url)
    response.raise_for_status()
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    articles = soup.find_all('article')
    parsed_articles = []

    for article in articles:
        # Extract the title and URL
        title_tag = article.find('h3', class_='entry-title')
        if title_tag and title_tag.a:
            title = title_tag.a.get_text(strip=True)
            article_url = title_tag.a['href']
        else:
            title = None
            article_url = None

        # Extract the date
        date_tag = article.find('time', class_='entry-date published')
        if date_tag:
            date = date_tag.get_text(strip=True)
        else:
            date = None

        # Check for "product page" and "press release" links
        if article_url:
            product_page_link, press_release_link = check_links(article_url)
        else:
            product_page_link, press_release_link = None, None

        parsed_articles.append({
            'title': title,
            'date': date,
            'product_page_link': product_page_link,
            'press_release_link': press_release_link
        })

    return parsed_articles

# Function to send data to Google Sheets via Google Apps Script
def send_to_google_sheets(data, web_app_url):
    response = requests.post(web_app_url, json=data)
    print(response.text)

# Parse multiple pages and send data one by one
def main():
    web_app_url = "https://script.google.com/macros/s/AKfycbz15ODMssXoLNeg3j0CMSUMPlQtnXE-zTt6lGz4nxCif3ItWhXP2FI_yzley4ZN4qqd2A/exec"  # Replace with your Google Apps Script web app URL
    serial_number = 1

    for page in range(1, 5):  # Example for pages 1 to 4
        articles = parse_main_page(page)
        
        for article in articles:
            article['serial'] = serial_number
            article['page'] = page
            send_to_google_sheets(article, web_app_url)
            serial_number += 1
            
            time.sleep(5)  # Sleep for 5 seconds between each link

        time.sleep(20)  # Sleep for 20 second after parsing each page

    sys.exit()  # Exit the script after processing all data

if __name__ == "__main__":
    main()
