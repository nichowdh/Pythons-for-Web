import requests
from bs4 import BeautifulSoup

def scrape_latest_news(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', class_='group text-black no-underline')
    
    news = []
    for article in articles:
        title = article.find('span', class_='text-lg text-black mb-3').text.strip()
        link = article['href']
        news.append({'title': title, 'link': link})
    
    return news

if __name__ == "__main__":
    latest_news = scrape_latest_news("https://www.quectel.com/company/news-and-pr/")
    for item in latest_news:
        print(item)
