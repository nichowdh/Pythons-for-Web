from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# Set up Selenium with Firefox in headless mode
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

# Open the URL
driver.get("https://www.microchip.com/en-us/about/news-releases")

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

entries = []

# Find all table rows with the role attribute set to 'row'
for row in soup.find_all('tr', role='row'):
    try:
        title_tag = row.find('td', class_='title-column dont_sort').find('a')
        date_tag = row.find_all('td')[1]
        
        if title_tag and date_tag:
            title = title_tag.get_text(strip=True)
            date = date_tag.get_text(strip=True)
            entries.append((title, date))
    except (AttributeError, IndexError) as e:
        # If any expected element is not found, skip this row
        continue

# Print the titles and dates
for title, date in entries:
    print(f"Title: {title}\nDate: {date}\n")

# Close the Selenium browser session
driver.quit()
