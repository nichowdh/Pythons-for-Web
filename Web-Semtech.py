import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.semtech.com/company/news-and-media")

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the media card containers
    cards = soup.find_all('div', class_='col-12 col-md-4 col-match-height')

    # List to hold parsed data
    articles = []

    # Extract the title and date from each card
    for card in cards:
        try:
            title_tag = card.find('p', class_='h5 text-green pt-2 text-start').find('a')
            title = title_tag.get_text(strip=True)
        except AttributeError:
            title = "No title found"

        try:
            date_tag = card.find('span', class_='entry-meta')
            date = date_tag.get_text(strip=True)
        except AttributeError:
            date = "No date found"

        articles.append({'title': title, 'date': date})

    # Print the extracted data
    for article in articles[:3]:
        print(f"Title: {article['title']}")
        print(f"Date: {article['date']}\n")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
