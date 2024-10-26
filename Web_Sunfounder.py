import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.sunfounder.com/blogs/news")

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all articles
    articles = soup.find_all('div', class_='block-list__item-blog')

    # Extract titles and dates
    entries = []
    for article in articles:
        title_tag = article.find('h2', class_='article-item__title').find('a')
        date_tag = article.find('time', class_='article-item__meta-item')
        
        if title_tag and date_tag:
            title = title_tag.text.strip()
            date = date_tag.text.strip()
            entries.append((title, date))

    # Print titles and dates
    for title, date in entries[:3]:
        print(f"Title: {title}\nDate: {date}\n")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
