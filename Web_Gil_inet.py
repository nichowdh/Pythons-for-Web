import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://blog.gl-inet.com/"
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all entries
entries = soup.find_all('div', class_='row')

# Initialize a list to store titles
titles = []

# Loop through each entry to extract title
for entry in entries:
    # Find the title
    title_container = entry.find('h3', class_='post-title')
    if title_container:
        title_tag = title_container.find('a')
        title = title_tag.get_text(strip=True) if title_tag else 'No title'
        titles.append(title)

# Print the titles
for title in titles:
    print(f"Title: {title}")
