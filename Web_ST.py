import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://newsroom.st.com/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
entries = soup.find_all('a', class_='swiper-slide stn-card stn-card--mobile-list')

for entry in entries:
    title_tag = entry.find('h3')
    date_tag = entry.find('div', class_='stn-card__date')

    if title_tag and date_tag:
        title = title_tag.get_text(strip=True)
        date = date_tag.get_text(strip=True)
        print(f"Title: {title}")
        print(f"Date: {date}")
        print('-' * 40)
