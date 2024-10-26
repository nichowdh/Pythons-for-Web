import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://smlight.tech/shop/?orderby=date")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

titles = [h2.text for h2 in soup.find_all('h2', class_='woocommerce-loop-product__title')]

for title in titles[:3]:
    print(title)
