import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = "https://revolutionpi.com/en/blog/"
response = requests.get(url, headers=headers)

def parse_entry_titles_and_dates(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    results = []
    for article in articles:
        # Extracting title
        title_element = article.find('h2', class_='entry-title')
        title = title_element.text.strip() if title_element else 'No Title Found'

        # Extracting date
        date_element = article.find('time', class_='entry-date published')
        date = date_element['datetime'] if date_element else 'No Date Found'

        results.append({'title': title, 'date': date})

    return results

# Example usage:
parsed_entries = parse_entry_titles_and_dates(response)

# Print parsed entries
for entry in parsed_entries[:3]:
    print(f"Title: {entry['title']}")
    print(f"Date: {entry['date']}")
    print("-" * 20)
