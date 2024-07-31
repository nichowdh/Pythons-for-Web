import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://hubitat.com/pages/press-releases")



# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
print("Press Release\n")

# Find all <p> elements within <div class="press-releases press__grid">
entries = soup.find_all('div', class_='press-releases press__grid')

# Extract title and date for each entry
for entry in entries[:3]:
    paragraphs = entry.find_all('p')
    for paragraph in paragraphs:
        date = paragraph.find('span').text.strip() if paragraph.find('span') else ''
        title = paragraph.find('a').text.strip() if paragraph.find('a') else ''
        print(f"Title: {title}")
        print(f"Date: {date}")
        print()
