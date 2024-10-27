
import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.nuvoton.com/news/news/all/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all rows with class 'css_tr'
rows = soup.find_all('div', class_='css_tr')

# Initialize lists to store dates and titles
dates = []
titles = []

# Iterate through each row to extract dates and titles
for row in rows[:4]:
    # Find all cells within the row
    cells = row.find_all('div', class_='css_td')
    
    # Ensure there are at least 2 cells (date and title)
    if len(cells) >= 2:
        date = cells[0].get_text(strip=True)
        title_tag = cells[1].find('a')
        
        if title_tag:
            title = title_tag.get('title', '').replace('&quot;', '"')
            dates.append(date)
            titles.append(title)

# Print the extracted dates and titles
for date, title in zip(dates, titles):
    print(f"Date: {date}, Title: {title}")
