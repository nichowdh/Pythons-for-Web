import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.sapphiretech.com/en/news")



# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')


# Extracting all the list items
list_items = soup.find_all('div', class_='listItem')

# Extracting dates and titles
entries = []
for item in list_items:
    date = item.find('time').text
    title = item.find('h3').text
    entries.append((date, title))

# Print the entries
for date, title in entries:
    print(f"Date: {date}, Title: {title}")
