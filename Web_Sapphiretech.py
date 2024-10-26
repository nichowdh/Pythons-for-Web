import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://www.sapphiretech.com/en/news"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

def parse_entries(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='listItem')

    results = []
    for entry in entries:
        # Extracting title
        title_element = entry.find('h3')
        title = title_element.text.strip() if title_element else 'No Title Found'

        # Extracting date
        date_element = entry.find('time')
        date = date_element.text.strip() if date_element else 'No Date Found'

        results.append({'title': title, 'date': date})

    return results

# Example usage:
parsed_entries = parse_entries(response)

# Print parsed entries
for entry in parsed_entries[:3]:
    print(f"Title: {entry['title']}")
    print(f"Date: {entry['date']}")
    print("-" * 20)
