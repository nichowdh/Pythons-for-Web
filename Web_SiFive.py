import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.sifive.com/press")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

entries = []

for article in soup.find_all('div', class_='PressReleases_article__Ca53e'):
    date_tag = article.find('p').text.split('—')[-1].strip()
    title_tag = article.find('a', class_='PressReleases_titleLink__T_E_d')
    if title_tag:
        title = title_tag.text.strip()
        entries.append((date_tag, title))

for date, title in entries[:3]:
    print(f"Date: {date}, Title: {title}")
