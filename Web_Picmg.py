import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.picmg.org/newsletter-archive/"

# Define headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://www.google.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

# Send a GET request to the URL with headers
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for request errors
except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
    exit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <p> tags within the entry-content div
entries = soup.select('.entry-content p')

if not entries:
    print("No entries found. The CSS selector might need adjustment.")

# Loop through each entry and extract the title and date
for entry in entries:
    a_tag = entry.find('a')
    if a_tag:
        title_date = a_tag.text
        # Split the title and date assuming the ' – ' delimiter is used
        if ' – ' in title_date:
            title, date = title_date.split(' – ', 1)
        else:
            title, date = title_date, 'No date found'
        print(f"Title: {title}\nDate: {date}\n")
    else:
        print("No <a> tag found in this entry.")
