import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://radxa.com/news/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize a list to store the titles and dates
    entries = []

    # Find all the list items
    news_items = soup.select('ul.news_TIAz > li')

    for index, item in enumerate(news_items):
        # Extract the title
        title_tag = item.select_one('div.new_t_gfEZ > h2')
        title = title_tag.text.strip() if title_tag else 'No title found'

        # Extract the date
        date_tag = item.select_one('p.time_soVr')
        date = date_tag.text.strip() if date_tag else 'No date found'

        # Append the title and date to the entries list
        entries.append((title, date))

       
    # Print the titles along with their dates
    for entry in entries:
        print(f"Title: {entry[0]}")
        print(f"Date: {entry[1]}")
        print()
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
