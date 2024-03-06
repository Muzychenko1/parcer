import requests
from bs4 import BeautifulSoup
def get_html(url):
    response = requests.get(url)
    return response.text

url = 'https://example.com'
html = get_html(url)
soup = BeautifulSoup(html, 'html.parser')


print(soup.prettify())