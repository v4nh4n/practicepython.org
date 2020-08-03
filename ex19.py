import requests
from bs4 import BeautifulSoup

base_url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(base_url)

soup = BeautifulSoup(r.text, features="html.parser")

a = soup.find_all("p", {"class":""})

for i in a[4:(len(a)-1)]:
    print(i.text)



