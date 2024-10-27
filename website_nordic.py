from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode (no GUI)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage
url = "https://www.nordicsemi.com/Nordic-news"
driver.get(url)

# Allow time for the page to load (adjust as necessary)
time.sleep(5)

# Retrieve the page source after JavaScript has rendered
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the driver
driver.quit()

# Find all news archive boxes
news_items = soup.find_all('div', class_='news-archive-box')

# Initialize a list to store the extracted data
news_data = []

# Extract titles and dates
for item in news_items:
    title_tag = item.find('div', class_='text-wrap')
    date_tag = item.find('div', class_='tag overlay')

    # Check if title and date tags are found
    if title_tag and date_tag:
        title = title_tag.get_text(strip=True)
        date = date_tag.get_text(strip=True)
        news_data.append((title, date))

# Print the extracted data
if news_data:
    for idx, (title, date) in enumerate(news_data[:3], start=1):  # Print only the latest 3 entries
        print(f"Entry {idx}:")
        print(f"Title: {title}")
        print(f"Date: {date}")
        print('-' * 40)
else:
    print("No news data extracted.")
