from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage
url = "https://www.renesas.com/us/en/about/newsroom#latest-press-releases"
driver.get(url)

# Allow time for the page to fully load (adjust as necessary)
time.sleep(5)

# Retrieve the page source after JavaScript has rendered
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the driver
driver.quit()

# Find all items with class 'item-wrapper press-releases-item-wrapper'
items = soup.find_all('div', class_='item-wrapper press-releases-item-wrapper')

# Initialize a list to store news items
news_data = []

# Loop through each item and extract title and date
for item in items:
    title_tag = item.find('div', class_='item-title press-releases-item-title')
    date_tag = item.find('time', class_='datetime press-releases-datetime')

    if title_tag and date_tag:
        title = title_tag.get_text(strip=True)
        date = date_tag['datetime']
        news_data.append((title, date))

# Print the latest 3 entries
for idx, (title, date) in enumerate(news_data[:3], start=1):
    print(f"Entry {idx}:")
    print(f"Title: {title}")
    print(f"Date: {date}")
    print("-" * 20)

if not news_data:
    print("No news data extracted.")
