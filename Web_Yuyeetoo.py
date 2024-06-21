import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.youyeetoo.com/blog/")


# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Initialize a list to store the titles and dates
entries = []

# Find all the divs with class 'blog_item'
blog_items = soup.find_all('div', class_='blog_item')

for item in blog_items:
    # Extract the date
    date_tag = item.find('div', class_='date')
    date = date_tag.text.strip() if date_tag else 'No date found'
    
    # Extract the title
    title_tag = item.find('div', class_='title')
    title = title_tag.text.strip() if title_tag else 'No title found'
    
    # Append the title and date to the entries list
    entries.append((title, date))

# Print the titles along with their dates
for entry in entries:
    print(f"Title: {entry[0]}")
    print(f"Date: {entry[1]}")
    print()
