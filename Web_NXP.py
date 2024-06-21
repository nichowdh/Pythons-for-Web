import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.nxp.com/company/about-nxp/newsroom:NEWSROOM")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
print("Press Release & News briefs\n")

entries = soup.find_all('div', class_='card1-item')

for entry in entries:
    title = entry.find('h3', class_='card1-title').text.strip()
    date = entry.find('p', class_='metadata').text.strip()
    print(f"Title: {title}\nDate: {date}\n")
