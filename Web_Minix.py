import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://theminixforum.com/index.php?forums/news-announcements.2/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
entries = []

# Find all structItems
struct_items = soup.find_all('div', class_='structItem')

for item in struct_items:
    title_tag = item.find('div', class_='structItem-title').find('a')
    title = title_tag.text.strip()
    
    date_tag = item.find('li', class_='structItem-startDate').find('time')
    date = date_tag['datetime']
    
    entries.append((title, date))

for entry in entries:
    print(f"Title: {entry[0]}, Date: {entry[1]}")
