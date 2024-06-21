import requests
from bs4 import BeautifulSoup

# URL of the news page
url = "https://www.cytron.io/tutorial/miscellaneous/news"

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

    # Initialize a list to store the titles and dates
    entries = []

    # Find all the divs with class 'blog-grid-item'
    blog_items = soup.find_all('div', class_='blog-grid-item')

    for item in blog_items:
        # Extract the title
        title_tag = item.find('h3').find('a')
        title = title_tag.text.strip() if title_tag else 'No title found'

        # Extract the date and author
        author_tag = item.find('div', class_='author').find('a')
        date_author_text = author_tag.text.strip() if author_tag else 'No date found'
        
        # Extract the date from the author text
        date = date_author_text.split(',')[-1].strip() if ',' in date_author_text else 'No date found'

        # Append the title and date to the entries list
        entries.append((title, date))

    # Print the titles along with their dates
    for entry in entries:
        print(f"Title: {entry[0]}")
        print(f"Date: {entry[1]}")
        print()
else:
    print(f"Error fetching the page: {response.status_code}")
