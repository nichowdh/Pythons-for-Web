import requests
from bs4 import BeautifulSoup

url = "https://www.emporiaenergy.com/blog/?e-filter-4847f41-category=news"

# Create a session object
session = requests.Session()

# Set headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}

# Send a GET request with headers
response = session.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all articles
    articles = soup.find_all('div', class_='elementor-element elementor-element-2d5d436c premium-header-inline elementor-widget elementor-widget-premium-addon-dual-header')

    # Extract titles and dates
    entries = []
    for article in articles:
        # Extract title
        title_tag = article.find('h2', class_='premium-dual-header-first-header')
        if title_tag:
            title = title_tag.text.strip()
        else:
            title = "No Title Found"
        
        # Extract date
        date_tag = article.find('time')
        if date_tag:
            date = date_tag.text.strip()
        else:
            date = "No Date Found"
        
        # Append title and date to entries list
        entries.append({"title": title, "date": date})

    # Print all extracted titles and dates
    for entry in entries:
        print(f"Title: {entry['title']}")
        print(f"Date: {entry['date']}")
        print()  # Empty line for readability
else:
    print(f"Failed to retrieve content, status code: {response.status_code}")
