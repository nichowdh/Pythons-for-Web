from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from googletrans import Translator

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode for performance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the URL
driver.get("https://wiki.sipeed.com/news/")

# Give the page some time to load content dynamically
driver.implicitly_wait(3)

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Extract all the entry titles
titles = [a.h2.get_text(strip=True) for a in soup.find_all('a', class_='blog_title')]

# Translate the titles to English
translator = Translator()
translated_titles = [translator.translate(title, src='zh-cn', dest='en').text for title in titles]

# Print the translated titles
for title in translated_titles[:3]:
    print(title)
