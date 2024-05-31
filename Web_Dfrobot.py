import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.dfrobot.com/blog")



# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# Extracting titles
titles = [title.text for title in soup.find_all('a', class_='title')]

# Print the titles
for title in titles:
    print(title)
