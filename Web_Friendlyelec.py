import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.friendlyelec.com/Forum/viewforum.php?f=3")

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Initialize a list to store the titles and dates
    entries = []

    # Find all the rows in the table
    rows = soup.find_all('tr', class_='t-row clickable')
    for row in rows:
        # Find the title
        title_tag = row.find('a', class_='topictitle')
        title = title_tag.text.strip() if title_tag else 'No title found'

        # Find the date
        date_tag = row.find('small')
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
