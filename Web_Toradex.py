import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.toradex.com/news")


soup = BeautifulSoup(response.content, 'html.parser')

# Find all the entries
entries = soup.find_all('div', class_='item d-flex')

for entry in entries[:3]:
    # Extract the date
    date = entry.find('div', class_='date').span.text.strip()
    # Extract the title
    title = entry.find('h5').text.strip()
    # Check for any additional title text in <p> tags
    additional_text = entry.find('div', class_='card-text').find('p')
    if additional_text:
        title += additional_text.text.strip()
        
    # Print the extracted information
    print(f"Date: {date}")
    print(f"Title: {title}")
    print('-' * 50)
