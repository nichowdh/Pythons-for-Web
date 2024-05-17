from bs4 import BeautifulSoup

# Sample HTML content
html_content = '''
<div class="card1 band" id="press-release">
    <section class="section-lead is-secondary">
      <div class="section-lead-header">
        <h2 class="section-lead-title">Featured Press Releases</h2>
      </div>
    </section>

    <div class="card1-list has-three is-tertiary">

        <div class="card1-column">
          <div class="card1-item">
            <figure class="card1-image">
              <img src="/assets/images/en/photography/FINANCIAL-RELEASE-IMG.jpg" alt="NXP Semiconductors Reports First Quarter 2024 Results Image">
            </figure>
            <div class="card1-header">
              <h3 class="card1-title">
                <a datavalue="NXP Semiconductors Reports First Quarter 2024 Results Click" href="https://media.nxp.com/news-releases/news-release-details/nxp-semiconductors-reports-first-quarter-2024-results">NXP Semiconductors Reports First Quarter 2024 Results</a>
              </h3>
              <p class="metadata">Apr 29, 2024</p>
            </div>
          </div>
        </div>

        <div class="card1-column">
          <div class="card1-item">
            <figure class="card1-image">
              <img src="/assets/images/en/photography/newsroom-thumbnail.png" alt="NXP Semiconductors Announces Conference Call to Review First Quarter 2024 Financial Results Image">
            </figure>
            <div class="card1-header">
              <h3 class="card1-title">
                <a datavalue="NXP Semiconductors Announces Conference Call to Review First Quarter 2024 Financial Results Click" href="/company/about-nxp/nxp-semiconductors-announces-conference-call-to-review-first-quarter-2024-financial-results:NW-NXP-CONFERENCE-CALL-FIRST-QUARTER-2024">NXP Semiconductors Announces Conference Call to Review First Quarter 2024 Financial Results</a>
              </h3>
              <p class="metadata">Apr 11, 2024</p>
            </div>
          </div>
        </div>

        <div class="card1-column">
          <div class="card1-item">
            <figure class="card1-image">
              <img src="/assets/images/en/photography/NW-NXP-BREAKS-THROUGH-OG.jpg" alt="NXP Breaks Through Integration Barriers for Software-Defined Vehicle Development with Open S32 CoreRide Platform Image">
            </figure>
            <div class="card1-header">
              <h3 class="card1-title">
                <a datavalue="NXP Breaks Through Integration Barriers for Software-Defined Vehicle Development with Open S32 CoreRide Platform Click" href="https://www.nxp.com/company/about-nxp/nxp-breaks-through-integration-barriers-for-software-defined-vehicle-development-with-open-s32-coreride-platform:NW-NXP-BREAKS-THROUGH-AB">NXP Breaks Through Integration Barriers for Software-Defined Vehicle Development with Open S32 CoreRide Platform</a>
              </h3>
              <p class="metadata">Mar 28, 2024</p>
            </div>
          </div>
        </div>

    </div>
    <br>
    <ul class="list-unstyled list-inline text-center mb0">
      <li>
        <a class="btn btn-lg" href="?collection=Media&amp;start=0&amp;max=12&amp;language=en&amp;query=typeNews>>Press%20Release">VIEW ALL PRESS RELEASES</a>
      </li>
    </ul>
</div>
'''

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with class 'card1-item'
items = soup.find_all('div', class_='card1-item')

# Initialize lists to store titles and dates
titles = []
dates = []

# Iterate through each item to extract titles and dates
for item in items:
    # Find the title
    title_tag = item.find('h3', class_='card1-title').find('a')
    if title_tag:
        title = title_tag.get_text(strip=True)
        titles.append(title)
    
    # Find the date
    date_tag = item.find('p', class_='metadata')
    if date_tag:
        date = date_tag.get_text(strip=True)
        dates.append(date)

# Print the extracted titles and dates
for title, date in zip(titles, dates):
    print(f"Date: {date}, Title: {title}")
