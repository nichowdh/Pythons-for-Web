import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.vecow.com/dispPageBox/vecow/VecowCP.aspx?ddsPageID=NEWS_EN")

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the list items
    list_items = soup.find_all('li')

    # Extract the titles and dates
    entries = []
    for item in list_items:
        title_div = item.find('div', class_='Title')
        date_div = item.find('div', class_='Date')
        if title_div and date_div:
            title = title_div.get_text(strip=True)
            date = date_div.get_text(strip=True)
            entries.append((title, date))

    # Print the results
    for title, date in entries:
        print(f"Title: {title}")
        print(f"Date: {date}")
        print("----------")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
