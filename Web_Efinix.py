import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request to the URL with the headers
response = requests.get("https://www.efinixinc.com/company-news.html", headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='col')

    for entry in entries[:3]:
        title_tag = entry.find('h4')
        date_tag = entry.find('span', class_='gray')

        if title_tag and date_tag:
            title = title_tag.get_text(strip=True)
            date = date_tag.get_text(strip=True)
            print(f"Title: {title}")
            print(f"Date: {date}")
            print()
        else:
            print("Title or date not found for an entry.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
