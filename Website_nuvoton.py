from bs4 import BeautifulSoup

# Sample HTML content
html_content = '''
<div class="table">
    <div class="table_container">
        <div class="css_table">
            <div class="css_tr">
                <div class="css_td td2">Date</div>
                <div class="css_td td3">Title</div>
            </div>
            <div class="css_tr">
                <div class="css_td">2024-05-03</div>
                <div class="css_td $">
                    <a href="/news/news/all/TSNuvotonNews-000508/" title="&quot;Nvovoton Technology 2024 Future Innovation Summit - Focusing on AI, New Energy, and Automotive Electronics&quot; is about to begin">
                        "Nvovoton Technology 2024 Future Innovation Summit - Focusing on AI, New Energy, and Automotive Electronics" is about to begin</a>
                </div>
            </div>
            <div class="css_tr">
                <div class="css_td">2024-05-03</div>
                <div class="css_td $">
                    <a href="/news/news/all/TSNuvotonNews-000506/" title="Nuvoton Technology Holds Investor Conference for the First Quarter of 2024">
                        Nuvoton Technology Holds Investor Conference for the First Quarter of 2024</a>
                </div>
            </div>
            <!-- Add other entries similarly -->
        </div>
    </div>
</div>
'''

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all rows with class 'css_tr'
rows = soup.find_all('div', class_='css_tr')

# Initialize lists to store dates and titles
dates = []
titles = []

# Iterate through each row to extract dates and titles
for row in rows:
    # Find all cells within the row
    cells = row.find_all('div', class_='css_td')
    
    # Ensure there are at least 2 cells (date and title)
    if len(cells) >= 2:
        date = cells[0].get_text(strip=True)
        title_tag = cells[1].find('a')
        
        if title_tag:
            title = title_tag.get('title', '').replace('&quot;', '"')
            dates.append(date)
            titles.append(title)

# Print the extracted dates and titles
for date, title in zip(dates, titles):
    print(f"Date: {date}, Title: {title}")
