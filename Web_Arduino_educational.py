import requests
from bs4 import BeautifulSoup


# Send a GET request to the URL
response = requests.get("https://www.arduino.cc/education/news/")



# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract title and date
title = soup.find('div', class_='card-item__title').text.strip()

# Since date is not provided in the snippet, assuming it needs to be fetched from another location.
# Let's assume the date is in a hypothetical element for illustration purposes.
# Replace 'date_element' with the actual element that contains the date in your specific case.

# Example assuming date is in a hypothetical element
date_element = soup.find('div', class_='card-item__date')
date = date_element.text.strip() if date_element else "Date Not Found"

# Print the extracted data
print(f"Title: {title}")
print(f"Date: {date}")
