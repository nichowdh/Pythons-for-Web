import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://community.geekompc.com/forums/official-news-and-deals.38/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all threads
threads = soup.find_all('div', class_='structItem')

# Initialize lists to store titles and dates
titles = []
dates = []

# Iterate through each thread to extract titles and dates
for thread in threads[:3]:
    # Find the title
    title_tag = thread.find('div', class_='structItem-title')
    if title_tag:
        title = title_tag.find_all('a')[-1].get_text(strip=True)  # The actual title link is the last <a> tag within the title div
        titles.append(title)
    
    # Find the date
    date_tag = thread.find('li', class_='structItem-startDate').find('time')
    if date_tag:
        date = date_tag.get_text(strip=True)
        dates.append(date)

# Print the extracted titles and dates
for title, date in zip(titles, dates):
    print(f"Date: {date}, Title: {title}")
    print()
