from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode for performance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the URL
url = "https://www.waveshare.com/new?dir=desc&order=position"
driver.get(url)

# Give the page some time to load content dynamically
driver.implicitly_wait(10)

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Extract all the product titles
titles = [h2.a.get_text(strip=True) for h2 in soup.find_all('h2', class_='product-name')]

# Print the titles
for title in titles[:3]:
    print(title)
