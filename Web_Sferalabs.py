import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = "https://sferalabs.cc/blog/"
response = requests.get(url, headers=headers)


def parse_entry_titles_and_dates(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('li')

    results = []
    for entry in entries:
        title_element = entry.find('h3', class_='fusion-title-heading')
        title = title_element.text.strip() if title_element else 'No Title Found'

        date_element = entry.find('span', class_='fusion-tb-published-date')
        date = date_element.text.strip() if date_element else 'No Date Found'

        # Ensure we have both title and date before appending
        if title != 'No Title Found' and date != 'No Date Found':
            results.append({'title': title, 'date': date})

    return results

# Example usage:
parsed_entries = parse_entry_titles_and_dates(response)

# Debugging prints
print(f"Number of entries found: {len(parsed_entries)}")
for entry in parsed_entries:
    print(f"Title: {entry['title']}")
    print(f"Date: {entry['date']}")
    print("-" * 20)
