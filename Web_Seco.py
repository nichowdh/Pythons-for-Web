from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize the WebDriver with headless option
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode for background execution
driver = webdriver.Chrome(options=options)

try:
    # Open the target URL
    url = "https://www.seco.com/news"
    driver.get(url)

    # Wait for the content to load by waiting for a 'media' div element
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'media'))
    )
    time.sleep(2)  # Extra wait to ensure all elements are fully loaded

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the latest 3 entries
    entries = soup.find_all('div', class_='media', limit=3)

    # Extract title and date for each entry
    for entry in entries:
        # Extract title
        title_element = entry.find('span', itemprop='headline')
        title = title_element.text.strip() if title_element else "Title not found"

        # Extract date
        date_element = entry.find('div', class_='card-text')
        date = date_element.text.strip() if date_element else "Date not found"

        # Print the results
        print(f"Title: {title}")
        print(f"Date: {date}\n")

finally:
    driver.quit()  # Close the browser instance
