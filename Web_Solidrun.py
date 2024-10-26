from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Set up Selenium with ChromeDriver using ChromeDriverManager
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navigate to the URL
driver.get("https://www.solid-run.com/press-room/")

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the driver
driver.quit()

entries = []

# Find all headers with the specified class
for header in soup.find_all('header', class_='entry-content-header'):
    # Extract the date
    date_tag = header.find('time', class_='av-magazine-time')
    if date_tag:
        date = date_tag.text.strip()
    else:
        date = 'No date found'

    # Extract the title
    title_tag = header.find('h3', class_='av-magazine-title')
    if title_tag:
        title = title_tag.text.strip()
        entries.append((date, title))

# Print the extracted data
for date, title in entries[:3]:
    print(f"Date: {date}, Title: {title}")
