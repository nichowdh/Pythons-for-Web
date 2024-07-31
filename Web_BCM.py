import requests
from bs4 import BeautifulSoup

# Define the URL
url = "https://www.bcmcom.com/bcm_enewsLetter.html"

# Define headers with a user-agent to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    # Send a GET request to the URL with headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <div> elements with class="row g-mx-5--sm g-mb-30"
        entries = soup.find_all('div', class_='row g-mx-5--sm g-mb-30')

        # Iterate through each entry to extract title and date
        for entry in entries[:3]:
            date = entry.find('p').text.strip()
            title = entry.find('h2').text.strip()
            print(f"Title: {title}\nDate: {date}\n")
    else:
        print(f"Failed to retrieve page: {url}. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching page: {url}. Exception: {e}")
