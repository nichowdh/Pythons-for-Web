import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Initialize the Selenium WebDriver (Make sure you have the correct WebDriver for your browser)
driver = webdriver.Chrome()  # Or use webdriver.Firefox() for Firefox

# URL of the news releases page
url = "https://www.qualcomm.com/news/releases"

# Open the URL
driver.get(url)

# Wait for the page to fully load (adjust the sleep time as needed)
time.sleep(5)

# Get the page source and parse it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Find all VerticalBlogCard containers
cards = soup.find_all('div', class_='VerticalBlogCard_container__2fwPS')
print(f"Found {len(cards)} cards")

# List to hold parsed data
articles = []

# Extract the title and date from each card
for card in cards:
    title_tag = card.find('a', class_='VerticalBlogCard_title__GUcB5')
    if title_tag:
        title = title_tag.get_text(strip=True)
    else:
        print("Title tag not found")
        title = "No Title"

    date_tag = card.find('div', class_='VerticalBlogCard_metaContainer__irnWk')
    if date_tag:
        date_span = date_tag.find('span')
        if date_span:
            date = date_span.get_text(strip=True)
        else:
            print("Date span not found")
            date = "No Date"
    else:
        print("Date tag not found")
        date = "No Date"

    articles.append({'title': title, 'date': date})

# Print the extracted data
for article in articles:
    print(f"Title: {article['title']}")
    print(f"Date: {article['date']}\n")

# Close the WebDriver
driver.quit()
