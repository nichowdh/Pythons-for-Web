import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.terra-master.com/global/press/")


# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Initialize a list to store the titles and dates
entries = []

# Find all the news items
news_items = soup.find_all('div', class_='news_list_item')

for item in news_items:
    # Extract the title
    title_tag = item.find('a')
    title = title_tag.text.strip() if title_tag else 'No title found'

    # Extract the date
    date_tag = item.find('div', class_='news_item_subtitle')
    date = date_tag.text.split('//')[0].strip() if date_tag else 'No date found'

    # Append the title and date to the entries list
    entries.append((title, date))

# Print the titles along with their dates
for entry in entries[:3]:
    print(f"Title: {entry[0]}")
    print(f"Date: {entry[1]}")
    print()
