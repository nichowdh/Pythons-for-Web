import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://news.lenovo.com/pressroom/press-releases/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

entries = soup.find_all('div', class_='card card-wide card-release')

for entry in entries:
    date = entry.find('small', class_='card-date card-list-date').text.strip()
    title = entry.find('h3', class_='card-title card-list-title').a.text.strip()
    print(f"Title: {title}, Date: {date}")
