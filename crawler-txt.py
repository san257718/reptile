import requests
from bs4 import BeautifulSoup



response = requests.get("https://www.ptt.cc/bbs/Food/index.html")

soup = BeautifulSoup(response.text, "lxml")

titles = soup.find_all("div",{"class":"title"})



with open("crawler.txt","w",encoding="utf-8") as file:
    for title in titles:
            file.write(title.text)
            print(title.getText().strip())