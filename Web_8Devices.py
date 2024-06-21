import requests
from bs4 import BeautifulSoup

# URL of the news page
url = "https://www.8devices.com/news"

# Custom headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send a GET request to the URL with custom headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize a list to store the titles
    titles = []

    # Find all the sections with the class 'single-post container'
    sections = soup.find_all('section', class_='single-post container')

    for section in sections[:5]:  # Limit to the first 3 entries
        # Extract the title
        title_tag = section.find('h3', class_='title')
        title = title_tag.text.strip() if title_tag else 'No title found'
        titles.append(title)

    # Print the titles
    for title in titles:
        print(f"Title: {title}")
else:
    print(f"Error fetching the page: {response.status_code}")
