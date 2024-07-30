from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# URL to scrape
url = "https://www.u-blox.com/en/newsroom"

# Configure Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode, comment out to see browser

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # Load the page
    driver.get(url)
    
    # Wait for the page to fully render (adjust as necessary)
    driver.implicitly_wait(5)  # seconds
    
    # Find all title elements
    titles = driver.find_elements(By.CSS_SELECTOR, 'a.intLink.w-full > h2.text-3xl')
    
    # Extract and print titles
    for title in titles[:3]:
        print(f"Title: {title.text.strip()}")
        print()
        
finally:
    # Close the browser
    driver.quit()
