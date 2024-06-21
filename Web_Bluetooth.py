import requests
from bs4 import BeautifulSoup

url = "https://www.bluetooth.com/events/"

headers = {
    "User-Agent": "Your User-Agent String",
    "Referer": "https://www.yourwebsite.com",  # Replace with an appropriate referer if needed
    "Accept-Language": "en-US,en;q=0.9",
    # Add more headers if required
}

try:
    # Send a GET request to the URL with headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    response.raise_for_status()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <article> elements
    articles = soup.find_all('article')

    # Iterate through each article to extract title and date
    for article in articles:
        # Extract title
        title_elem = article.find('h4', class_='card-title')
        title = title_elem.text.strip() if title_elem else "No title found"

        # Extract date
        date_elem = article.find('li', class_='date')
        date = date_elem.text.strip() if date_elem else "No date found"

        print(f"Title: {title}\nDate: {date}\n")

except requests.exceptions.RequestException as e:
    print(f"Error fetching page: {e}")

except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
