import requests
from bs4 import BeautifulSoup

base_url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(base_url)

soup = BeautifulSoup(r.text, features="html.parser")

a = soup.find_all("p", {"class":""})
text = ""

for i in a[4:(len(a)-1)]:
    first_half = i.text[:len(i.text)//8]
    second_half = i.text[len(i.text)//8+1:]
    text+=first_half+"\n"+second_half+"\n"

with open("C:\\Users\\v4h4\\Desktop\\file.txt","w", encoding="utf8") as file:
    file.write(text)



