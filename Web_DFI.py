import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://www.dfi.com/pressroom?news=0"
response = requests.get(url)

def parse_entries(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('a', class_='item')

    results = []
    for entry in entries:
        # Extracting title
        title_element = entry.find('h3', class_='title')
        title = title_element.text.strip() if title_element else 'No Title Found'

        # Extracting date
        date_element = entry.find('div', class_='date')
        date = date_element.text.strip() if date_element else 'No Date Found'

        results.append({'title': title, 'date': date})

    return results

# Example usage:
parsed_entries = parse_entries(response)

# Print parsed entries
for entry in parsed_entries:
    print(f"Title: {entry['title']}")
    print(f"Date: {entry['date']}")
    print("-" * 20)
