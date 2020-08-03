import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")
title = soup.find_all('h2')

print(title)
