
import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.makerfabs.com/blog")



soup = BeautifulSoup(response.content, 'html.parser')

# Find all divs with class 'post-item'
items = soup.find_all('div', class_='post-item')

# Initialize lists to store titles and dates
titles = []
dates = []

# Iterate through each item to extract titles and dates
for item in items:
    # Find the title
    title_tag = item.find('span', class_='post-title')
    if title_tag:
        title = title_tag.get_text(strip=True)
        titles.append(title)
    
    # Find the date
    date_tag = item.find('div', class_='post-posed-date')
    if date_tag:
        date = date_tag.get_text(strip=True)
        dates.append(date)

# Print the extracted titles and dates
for title, date in zip(titles, dates):
    print(f"Date: {date}, Title: {title}")