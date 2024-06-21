import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://ctl.net/blogs/insights")



# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all article items
article_items = soup.find_all('div', class_='article-item')

# List to hold parsed data
articles = []

# Extract the title, URL, and date from each article item
for item in article_items:
    title_tag = item.find('h3', class_='article-item__title')
    title = title_tag.get_text(strip=True)
    date = item.find('time', class_='article__meta-item article__date').get_text(strip=True)
    articles.append({'title': title, 'date': date})

# Print the extracted data
for article in articles:
    print(f"Title: {article['title']}")
    print(f"Date: {article['date']}\n")
