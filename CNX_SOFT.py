import requests
from bs4 import BeautifulSoup

# Function to check for "product page" and "press release" links in an article
def check_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    product_page_link = None
    press_release_link = None
    
    # Look for links containing "product page" and "press release"
    for a_tag in soup.find_all('a', href=True):
        if 'product page' in a_tag.get_text(strip=True).lower():
            product_page_link = a_tag['href']
        if 'press release' in a_tag.get_text(strip=True).lower():
            press_release_link = a_tag['href']
    
    return product_page_link, press_release_link

# Send a GET request to the main URL
response = requests.get("https://www.cnx-software.com/page/2/")
response.raise_for_status()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('article')

parsed_articles = []

for article in articles:
    # Extract the title and URL
    title_tag = article.find('h3', class_='entry-title')
    if title_tag and title_tag.a:
        title = title_tag.a.get_text(strip=True)
        article_url = title_tag.a['href']
    else:
        title = None
        article_url = None

    # Extract the date
    date_tag = article.find('time', class_='entry-date published')
    if date_tag:
        date = date_tag.get_text(strip=True)
    else:
        date = None

    # Extract the author
    author_tag = article.find('span', class_='author vcard')
    if author_tag:
        author = author_tag.get_text(strip=True)
    else:
        author = None
    
    # Check for "product page" and "press release" links
    if article_url:
        product_page_link, press_release_link = check_links(article_url)
    else:
        product_page_link, press_release_link = None, None
    
    parsed_articles.append({
        'title': title,
        'date': date,
        'author': author,
        'article_url': article_url,
        'product_page_link': product_page_link,
        'press_release_link': press_release_link
    })

# Print the parsed articles
for entry in parsed_articles:
    print(f"Title: {entry['title']}\nDate: {entry['date']}\nAuthor: {entry['author']}\nArticle URL: {entry['article_url']}\nProduct Page Link: {entry['product_page_link']}\nPress Release Link: {entry['press_release_link']}\n")
