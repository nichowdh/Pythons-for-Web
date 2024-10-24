import requests
from bs4 import BeautifulSoup

# URL of the Hubitat blog
url = "https://hubitat.com/blog"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all blog entries (modify this selector if necessary)
    entries = soup.find_all('div', class_='BlogItem_item__OCiDd')

    # Initialize a list to store titles and dates
    titles_dates = []

    # Loop through the first 3 entries to extract titles and dates
    for entry in entries[:3]:  # Limit to the first 3 entries
        # Extract the title
        title_container = entry.find('h2', class_='BlogItem_title__9_nUp')
        title = title_container.get_text(strip=True) if title_container else 'No title found'

        # Extract the date
        date_container = entry.find('p', class_='BlogItem_date__NaQEt')
        date = date_container.get_text(strip=True) if date_container else 'No date found'

        titles_dates.append((date, title))

    # Print the titles and dates
    for date, title in titles_dates:
        print(f"Date: {date}")
        print(f"Title: {title}\n")
else:
    print(f"Failed to retrieve content, status code: {response.status_code}")
