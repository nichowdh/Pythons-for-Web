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

    # Find all the article links (news-article-card)
    articles = soup.find_all('a', class_='news-article-card')

    if not articles:
        print("No articles found.")

    # Loop through the first 3 articles and extract the titles
    for article in articles[:3]:
        # Find the <h3> tag inside each article
        title_tag = article.find('h3', class_='brxe-uzsxwg brxe-heading h6')
        title = title_tag.text.strip() if title_tag else 'No title found'
        titles.append(title)

    # Print the titles
    for title in titles:
        print(f"Title: {title}\n")
else:
    print(f"Error fetching the page: {response.status_code}")
