from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Configure the Selenium WebDriver to use a headless browser
options = Options()
options.headless = True

try:
    # Set up the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to the URL
    driver.get("https://news.avnet.com/overview/default.aspx")

    # Wait for the module items to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "module_item"))
    )

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all the module items
    module_items = soup.find_all('div', class_='module_item')

    # Extract the titles and dates
    entries = []
    for item in module_items:
        headline_div = item.find('div', class_='module_headline')
        date_span = item.find('span', class_='module_date-text')
        if headline_div and date_span:
            title = headline_div.get_text(strip=True)
            date = date_span.get_text(strip=True)
            entries.append((title, date))

    # Print the results
    for title, date in entries:
        print(f"Title: {title}")
        print(f"Date: {date}")
        print("----------")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
