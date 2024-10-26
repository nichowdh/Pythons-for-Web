import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.smartcow.ai/press-releases-home")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
entries = soup.find_all('div', class_='w-dyn-item')

for entry in entries[:5]:
    title_tag = entry.find('h1', class_='display-s-light')
    date_tag = entry.find('div', class_='text-m-reg has--n700-text')

    if title_tag and date_tag:
        title = title_tag.get_text(strip=True)
        date = date_tag.get_text(strip=True)
        print(f"Title: {title}")
        print(f"Date: {date}")
        print('-' * 40)
