import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.formuler.tv/news")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the articles
articles = soup.find_all('article', {'data-hook': 'post-list-item'})

# Extract titles and dates
entries = []
for article in articles[:3]:
    title_tag = article.find('div', {'data-hook': 'post-title'})
    date_tag = article.find('span', {'data-hook': 'time-ago'})
    
    if title_tag and date_tag:
        title = title_tag.get_text(strip=True)
        date = date_tag.get_text(strip=True)
        entries.append((title, date))

# Print the entries
for title, date in entries:
    print(f"Title: {title}, Date: {date}")
