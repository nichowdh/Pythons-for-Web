import requests
from bs4 import BeautifulSoup

# Set headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a GET request to the URL
response = requests.get("https://www.myirtech.com/news.asp", headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the relevant table rows
    rows = soup.find_all('tr')

    entries = set()  # Use a set to store unique entries

    # Iterate over each row to extract the title and date
    for row in rows:
        title_tag = row.find('a', title=True)
        date_tag = row.find('td', width="10%")

        if title_tag and date_tag:
            title = title_tag.get('title', '').strip()
            date = date_tag.get_text(strip=True)
            entries.add((title, date))  # Add to set to ensure uniqueness

    # Print the extracted entries
    for title, date in entries:
        print(f"Title: {title}, Date: {date}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
