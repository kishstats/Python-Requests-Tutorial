import requests
from bs4 import BeautifulSoup

url = 'https://www.cia.gov/library/publications/the-world-factbook/rankorder/2004rank.html'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
table = soup.find(id='rankOrder')
rows = table.find_all('tr')

for row in rows:
    target_column = row.find_all('td', 'region')
    if target_column:
        link = target_column[0].find('a')
        href = link['href']

        idx_html = href.index('.html')
        country_code = href[idx_html-2:idx_html]

        print('country_code: {}'.format(country_code))
