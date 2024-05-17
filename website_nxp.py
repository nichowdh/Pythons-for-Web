
import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.nxp.com/company/about-nxp/newsroom:NEWSROOM")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all divs with class 'card1-item'
items = soup.find_all('div', class_='card1-item')

# Initialize lists to store titles and dates
titles = []
dates = []

# Iterate through each item to extract titles and dates
for item in items:
    # Find the title
    title_tag = item.find('h3', class_='card1-title').find('a')
    if title_tag:
        title = title_tag.get_text(strip=True)
        titles.append(title)
    
    # Find the date
    date_tag = item.find('p', class_='metadata')
    if date_tag:
        date = date_tag.get_text(strip=True)
        dates.append(date)

# Print the extracted titles and dates
for title, date in zip(titles, dates):
    print(f"Date: {date}, Title: {title}")
