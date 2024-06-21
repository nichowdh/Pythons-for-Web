import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://portwell.com/productnews.php"

try:
    # Send a GET request to the URL with SSL verification disabled
    response = requests.get(url, verify=False)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Initialize a list to store the titles and dates
    entries = []

    # Find all the table rows
    rows = soup.find_all('tr')

    for row in rows[:3]:  # Limit to the first 3 entries
        # Extract the title
        title_tag = row.find('a', class_='pr-title')
        title = title_tag.text.strip() if title_tag else 'No title found'

        # Extract the date
        date_tag = row.find('small')
        date = date_tag.text.strip() if date_tag else 'No date found'

        # Append the title and date to the entries list
        entries.append((title, date))

    # Print the titles along with their dates
    for entry in entries:
        print(f"Title: {entry[0]}")
        print(f"Date: {entry[1]}")
        print()

except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
