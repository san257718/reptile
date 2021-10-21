import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook



response = requests.get("https://www.ptt.cc/bbs/Food/index.html")

soup = BeautifulSoup(response.text, "lxml")

titles = soup.find_all("div",{"class":"title"})

wb = Workbook()
ws = wb.active
titla = []
ws.append(titla)



for title in titles:
    for i in title:
        ws.append(list(i))
        print(title.getText().strip())
        wb.save("crawler.xlsx")
    



