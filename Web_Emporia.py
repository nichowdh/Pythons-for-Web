from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

# URL of the blog page
url = "https://www.emporiaenergy.com/blog/?e-filter-4847f41-category=news"
driver.get(url)

# Allow time for the page to fully load
time.sleep(5)  # Adjust as needed

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the Selenium WebDriver
driver.quit()

# Find all articles
articles = soup.find_all('div', class_='elementor-element elementor-element-2d5d436c premium-header-inline elementor-widget elementor-widget-premium-addon-dual-header')

# Extract titles and dates
entries = []
for article in articles[:3]:
    # Extract title
    title_tag = article.find('h2', class_='premium-dual-header-first-header')
    title = title_tag.text.strip() if title_tag else "No Title Found"

    # Extract date
    date_tag = article.find('time')
    date = date_tag.text.strip() if date_tag else "No Date Found"
    
    # Append title and date to entries list
    entries.append({"title": title, "date": date})

# Print all extracted titles and dates
for entry in entries:
    print(f"Title: {entry['title']}")
    print(f"Date: {entry['date']}")
    print()  # Empty line for readability
