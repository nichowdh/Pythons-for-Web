import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://www.mekotronics.com/h-col-104.html"

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request to the URL
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the product titles
    titles = [a['title'] for a in soup.find_all('a', class_='fk-productName')]

    # Print the titles
    for title in titles[:5]:
        print(title)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
