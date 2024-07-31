from bs4 import BeautifulSoup
import requests

# URL of the webpage containing the HTML structure
url = "https://www.beagleboard.org/blog/"

# Send a GET request to fetch the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with class 'feature-card'
entries = soup.find_all('div', class_='feature-card')

# Iterate over each entry to extract title, URL, and date
for entry in entries[:3]:
    # Extract the title
    title_element = entry.find('p', class_='card-title')
    if title_element:
        title = title_element.text.strip()
    else:
        title = "No title found"

    # Print the extracted information
    print(f"Title: {title}")
    print()
