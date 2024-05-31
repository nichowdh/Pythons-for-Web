import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Send a GET request to the URL
response = requests.get("https://www.spacetouch.co/cat47")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Initialize the translator
translator = Translator()

# Find all entries
entries = soup.find_all("div", class_="nwom")

# Iterate through the entries and extract titles
for entry in entries:
    title_tag = entry.find("div", class_="sim s24")
    if title_tag:
        title = title_tag.get_text(strip=True)
        # Translate the title to English
        translated_title = translator.translate(title, src='zh-cn', dest='en').text
        print("Entry Title:", translated_title)
