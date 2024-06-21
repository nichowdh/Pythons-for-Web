import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.collabora.com/news-and-blog/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all entries
entries = soup.find_all('div', class_='BlogAndNewsArticleTplWrapper')

# Extract the first 3 entry titles and dates
for entry in entries[:5]:
    title_tag = entry.find('h3').find('a')
    date_tag = entry.find('p', class_='_2016datestamp').find('strong')

    title = title_tag.get_text(strip=True)
    date = date_tag.get_text(strip=True)

    print(f"Title: {title}, Date: {date}")
