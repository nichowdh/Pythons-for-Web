from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up the WebDriver (assuming ChromeDriver is in your PATH)
driver = webdriver.Chrome()

# URL of the webpage to scrape
url = "https://www.adata.com/in/news/"
driver.get(url)

try:
    # Wait until the news items are loaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'style_card-frame__On5UP'))
    )

    # Get page source after JavaScript has executed
    page_source = driver.page_source

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Select news items based on the observed structure
    news_items = soup.select('.style_card-frame__On5UP')

    

    for item in news_items[:3]:
        # Extract the title
        title_tag = item.select_one('.style_card-title__Elqfd')
        title = title_tag.text.strip() if title_tag else 'No title found'

        # Extract the date
        day_tag = item.select_one('.style_card-date-frame__1XNWi')
        month_tag = item.select_one('.style_card-date-year__4VAtT p:nth-of-type(2)')
        year_tag = item.select_one('.style_card-date-year__4VAtT p:nth-of-type(1)')

        day = day_tag.text.strip() if day_tag else 'No day found'
        month = month_tag.text.strip() if month_tag else 'No month found'
        year = year_tag.text.strip() if year_tag else 'No year found'

        date = f'{day} {month} {year}'

        print(f'Title: {title}, Date: {date}')
        print()
finally:
    # Close the WebDriver
    driver.quit()
