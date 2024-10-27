from selenium import webdriver
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

# URL of the website to scrape
url = "https://www.asrockind.com/en-gb/article-category/19"

# Navigate to the URL
driver.get(url)

# Wait for the page to fully load
driver.implicitly_wait(10)

# Get page source
html = driver.page_source

# Close the WebDriver
driver.quit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all article entries
articles = soup.find_all('div', class_='box-1 border-bottom pb-3 pt-3 pl-md-3')

# Extract titles and dates
entries = []
for article in articles:
    # Extract date
    date_tag = article.find('span', class_='date')
    if date_tag:
        date = date_tag.text.strip()
    else:
        date = "No Date Found"
    
    # Extract title
    title_tag = article.find('h4')
    if title_tag:
        title = title_tag.text.strip()
    else:
        title = "No Title Found"
    
    # Append title and date to entries list
    entries.append({"title": title, "date": date})

# Print all extracted titles and dates
for entry in entries[:3]:
    print(f"Title: {entry['title']}")
    print(f"Date: {entry['date']}")
    print()  # Empty line for readability
