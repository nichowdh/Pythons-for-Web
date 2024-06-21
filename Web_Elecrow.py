import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.elecrow.com/blog/elecrow-news")

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize lists to store titles and dates
    titles = []
    dates = []

    # Find all the post-item elements
    posts = soup.find_all('li', class_='post-item')

    # Loop through each post and extract the title and date
    for post in posts:
        # Extract the title
        title = post.find('h3', class_='post-title').get_text(strip=True)
        titles.append(title)

        # Extract the date
        date = post.find('span', class_='post-date').get_text(strip=True)
        dates.append(date)

    # Print the extracted titles and dates
    for i, (title, date) in enumerate(zip(titles, dates), 1):
        print(f"Post {i}:")
        print(f"Title: {title}")
        print(f"Date: {date}\n")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
