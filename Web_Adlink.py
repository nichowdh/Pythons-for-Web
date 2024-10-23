from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up Selenium WebDriver with options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL of the webpage to scrape
url = "https://www.adlinktech.com/en/news"

try:
    # Open the URL
    driver.get(url)

    # Wait for the news section to load (adjust the element you're waiting for if necessary)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'latest-news'))
    )

    # Get the page source after JavaScript has rendered
    page_source = driver.page_source

    # Print the page source to check if content is loaded correctly
    # (You can comment this out after confirming the correct content is loaded)
    # print(page_source)

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all the news entries
    news_entries = soup.find_all('a', class_='latest-news')

    # Print the number of news entries found
    print(f"Number of news entries found: {len(news_entries)}")

    # Extract the titles and dates
    news_data = []
    for entry in news_entries[:3]:
        title = entry.find('h3', class_='news-header-3').get_text(strip=True) if entry.find('h3', class_='news-header-3') else 'No title found'
        date = entry.find('p', class_='sub-info-date').get_text(strip=True) if entry.find('p', class_='sub-info-date') else 'No date found'
        news_data.append({'title': title, 'date': date})

    # Print the extracted data
    for news in news_data:
        print(f"Title: {news['title']}")
        print(f"Date: {news['date']}")
        print()

finally:
    # Quit the WebDriver
    driver.quit()
