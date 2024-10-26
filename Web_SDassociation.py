import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.sdcard.org/press/whatsnew/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
entries = []

for li in soup.find_all('li'):
    date_tag = li.find('time', class_='updated entry-time')
    if date_tag:
        date = date_tag.get('datetime', '').strip()
        title_tag = li.find('span', class_='bold')
        if title_tag and title_tag.a:
            title = title_tag.a.text.strip()
        else:
            title = title_tag.text.strip() if title_tag else ''
        entries.append((date, title))

for date, title in entries[:3]:
    print(f"Date: {date}, Title: {title}")
