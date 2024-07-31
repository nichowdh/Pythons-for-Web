import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.ecsipc.com/en/news")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all news entries
entries = soup.find_all('div', class_='item')
print("News List: \n")
# Print the news entries with titles and dates
for entry in entries[:3]:
    date_tag = entry.find('div', class_='tag-date').find('span', class_='name')
    date = date_tag.get_text(strip=True) if date_tag else 'No date'
    title_tag = entry.find('h4').find('a', class_='title')
    title = title_tag.get_text(strip=True) if title_tag else 'No title'
    print(f"Title: {title}")
    print(f"Date: {date}\n")
