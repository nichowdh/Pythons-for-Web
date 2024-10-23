from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://developer.android.com/news"

try:
    # Load the webpage
    driver.get(url)

    # Wait for the page to load completely by waiting for an element with 'devsite-card-wrapper'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "devsite-card-wrapper"))
    )

    # Get the page source after it's fully loaded
    page_source = driver.page_source

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all the entries (card wrappers)
    entries = soup.find_all('div', class_='devsite-card-wrapper')

    if not entries:
        print("No entries found on the page.")
    else:
        # Extract titles for the first 5 entries
        for entry in entries[:3]:
            title = entry.get('displaytitle', 'No title found')
            print(f"Title: {title}")
            print()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the driver
    driver.quit()
