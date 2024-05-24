import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.nordicsemi.com/Nordic-news")

# Initialize BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all news archive boxes
news_items = soup.find_all('div', class_='news-archive-box')

# Initialize a list to store the extracted data
news_data = []

# Extract titles and dates
for item in news_items:
    title_tag = item.find('div', class_='text-wrap').find('p')
    date_tag = item.find('div', class_='tag overlay').find('div', class_='date')
    
    if title_tag and date_tag:
        title = title_tag.text.strip()
        date = date_tag.text.strip()
        news_data.append((title, date))

# Print the extracted data
for title, date in news_data:
    print(f"Title: {title}\nDate: {date}\n")
