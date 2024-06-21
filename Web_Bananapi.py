import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://banana-pi.org/en/bananapi-news/")

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize a list to store the titles
    titles = []

    # Find all the <h2> tags within <dd> elements
    h2_tags = soup.find_all('h2')

    for tag in h2_tags:
        # Extract the title text
        title = tag.text.strip()
        titles.append(title)

    # Print the titles
    for title in titles:
        print(f"Title: {title}")
else:
    print(f"Error fetching the page: {response.status_code}")
