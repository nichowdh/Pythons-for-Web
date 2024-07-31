import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://gettobyte.in/semiconductor-chip-blogs/")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all elements with class 'serv-box-2 s2' within the provided HTML content
entries = soup.find_all('div', class_='serv-box-2 s2')

# Iterate over each entry and extract the title
for entry in entries[:3]:
    # Extract the title from <h5> tag
    title = entry.find('h5').text.strip()
    print("Entry Title:", title)
    print()
