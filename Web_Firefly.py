import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://en.t-firefly.com/news.html")



# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# Find all news entries
entries = soup.find_all('div', class_='news-list')

# Print all news entries with titles and dates
for i, entry in enumerate(entries[:3]):  # Limit to first  entries
    title_tag = entry.find('h4').find('a')
    title = title_tag.get_text(strip=True) if title_tag else 'No title'
    date_tag = entry.find('div', class_='other').find('span')
    date = date_tag.get_text(strip=True) if date_tag else 'No date'
    print(f"Title: {title}")
    print(f"Date: {date}\n")
