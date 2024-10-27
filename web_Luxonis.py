from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode, comment out to see browser actions

# Setup Chrome service
service = Service(ChromeDriverManager().install())

# Create WebDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the URL
url = "https://discuss.luxonis.com/blog"

try:
    # Load the page
    driver.get(url)

    # Wait for the page to load
    driver.implicitly_wait(10)  # Adjust the wait time as needed

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    entries = []

    # Find all <a> elements with class 'BlogList-item'
    for item in soup.find_all('a', class_='BlogList-item')[:3]:
        title_tag = item.find('h4')
        
        if title_tag:
            title = title_tag.get_text(strip=True)
            entries.append(title)

    # Print the titles
    if entries:
        for title in entries:
            print(f"Title: {title}")
    else:
        print("No blog titles found.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the WebDriver
    driver.quit()
