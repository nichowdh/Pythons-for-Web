import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.elegoo.com/pages/blog-collection#3d")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the blog post divs
blog_posts = soup.find_all('div', class_='blog-post')

# Extract titles and dates
for post in blog_posts:
    title = post.find('h5').get_text(strip=True)
    date = post.find('aside', class_='post-meta').get_text(strip=True)
    print(f'Title: {title}')
    print(f'Date: {date}')
    print()
