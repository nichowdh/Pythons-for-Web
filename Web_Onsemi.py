import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.onsemi.com/company/news-media/in-the-news")

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all entries
    entries = soup.find_all('div', class_='card')

    # Loop through each entry and extract the title and date
    for entry in entries[:3]:
        # Extract the date
        date_tag = entry.find('p').find('span')
        date = date_tag.text if date_tag else 'No date found'
        
        # Extract the title
        title_tag = entry.find('h6').find('a')
        title = title_tag.text if title_tag else 'No title found'
        
        print(f"Title: {title}\nDate: {date}\n")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
