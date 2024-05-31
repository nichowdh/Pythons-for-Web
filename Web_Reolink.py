import requests
from bs4 import BeautifulSoup

# Set the headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

# Send a GET request to the URL
response = requests.get("https://reolink.com/blog/category/news/", headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')  

    # Find all the article blocks
    articles = soup.find_all('div', class_='wXzZUXnMGtTud3SFxLJy')
    
    # Debug: Print the number of articles found
    print(f"Number of articles found: {len(articles)}")
    
    # Extract the titles and dates
    entries = []
    for article in articles:
        # Debug: Print the article content
        title_tag = article.find('p', class_='xEzQ_N4GjtoQnoV_M9Bv').find('a') if article.find('p', class_='xEzQ_N4GjtoQnoV_M9Bv') else None
        date_tag = article.find('p', class_='TWnkX91XGjrLqaDYn59f')
            
        
        if title_tag and date_tag:
            title = title_tag.get_text(strip=True)
            date = date_tag.get_text(strip=True)
            entries.append((title, date))

    # Display the titles and dates
    for index, (title, date) in enumerate(entries, start=1):
        print(f"Entry {index}:")
        print(f"Title: {title}")
        print(f"Date: {date}\n")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
