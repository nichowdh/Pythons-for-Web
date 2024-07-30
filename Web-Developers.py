from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
    
    # Wait for the page to load completely (adjust wait time as needed)
    driver.implicitly_wait(10)
    
    # Get the page source after it's fully loaded
    page_source = driver.page_source
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all entries
    entries = soup.find_all('div', class_='devsite-card-wrapper')

    if not entries:
        print("No entries found on the page.")

    # Extract title and date for each entry
    for entry in entries[:3]:
        title = entry.get('displaytitle', '')
        date = entry.find('p', class_='devsite-card-date').text.strip() if entry.find('p', class_='devsite-card-date') else ''
        print(f"Title: {title}")
        print(f"Date: {date}")
        print()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the driver
    driver.quit()
