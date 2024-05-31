import requests
from bs4 import BeautifulSoup

url = "https://blog.arduino.cc/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article', class_='post')
    if articles:
        for article in articles:
            title_elem = article.find('h2', itemprop='name headline')
            if title_elem:
                title = title_elem.text.strip()
                print(f"Title: {title}")
            else:
                print("Title not found for an article")
    else:
        print("No articles found")
else:
    print(f"Failed to retrieve page: {response.status_code}")
