import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://edgeimpulse.com/blog/")



# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

entries = soup.find_all('article', class_='flex')

for entry in entries:
    title = entry.find('h3').text.strip()
    date = entry.find('time')['datetime']
    print(f'Title: {title}\nDate: {date}\n')
