import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://toshiba.semicon-storage.com/ap-en/company/news.html"
response = requests.get(url)

# Check the status of the request
if response.status_code != 200:
    print(f"Failed to retrieve page: {url}")
    print(f"Status code: {response.status_code}")
    exit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <dl> elements within the specified <div> class
entries = soup.find_all('dl')

# Extract titles and dates from each <dl> element
entry_data = []
for entry in entries:
    date_tag = entry.find('dt')
    title_tag = entry.find('dd', class_='comp_v3_0990__newslist__caption')
    if date_tag and title_tag:
        date = date_tag.get_text(strip=True)
        title = title_tag.get_text(strip=True)
        entry_data.append({'title': title, 'date': date})

# Print all extracted data
if entry_data:
    for idx, entry in enumerate(entry_data, start=1):
        print(f"Entry {idx}:")
        print(f"Date: {entry['date']}")
        print(f"Title: {entry['title']}")
        print()
else:
    print("No entry data extracted.")
