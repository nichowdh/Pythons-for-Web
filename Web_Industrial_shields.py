from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.headless = True  # Run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL of the blog page
url = "https://www.industrialshields.com/blog/arduino-raspberry-pi-industrial-news-industry-4-0-iot-11"

# Open the webpage
driver.get(url)

# Wait for the page to load completely
time.sleep(5)

# Get the page source
html_content = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all articles
articles = soup.find_all('article', class_='o_wblog_post')

# Extract titles
titles = []
for article in articles:
    title_tag = article.find('a', class_='o_blog_post_title')
    if title_tag:
        title = title_tag.text.strip()
        titles.append(title)

# Print titles
for title in titles:
    print(title)
