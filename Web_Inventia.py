from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Set up Selenium with headless mode (optional)
options = Options()
options.headless = True
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Load the webpage
driver.get("https://inventia.online/news/")

# Wait for the page to load completely (adjust the sleep time if necessary)
import time
time.sleep(5)

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
titles = []

# Find all the h4 elements containing the titles
for h4 in soup.find_all('h4'):
    a_tag = h4.find('a')
    if a_tag:
        titles.append(a_tag.get_text())

# Print the extracted titles
if titles:
    for title in titles:
        print(title)
else:
    print("No titles found")

# Close the browser
driver.quit()
