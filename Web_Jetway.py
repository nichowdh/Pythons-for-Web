import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://jetwayipc.com/jetwaynews/?lang=en")



# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting all the post titles
post_items = soup.find_all('div', class_='post-item')

# Extracting titles
titles = []
for item in post_items[:3]:
    title = item.find('h5', class_='post-title').text.strip()
    titles.append(title)

# Print the titles
for title in titles:
    print(f"Title: {title}")
