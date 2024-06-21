import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://zeus.ugent.be/blog/23-24/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

entries = []

for blog_preview in soup.find_all('div', class_='content blog-preview'):
    title_tag = blog_preview.find('a', class_='title')
    date_tag = blog_preview.find('small', class_='column blogpreview-extra')
    
    title = title_tag.text.strip() if title_tag else 'No title'
    date = date_tag.text.split(' • ')[0].strip() if date_tag else 'No date'
    
    entries.append({'title': title, 'date': date})

for entry in entries:
    print(f"Title: {entry['title']}, Date: {entry['date']}")
