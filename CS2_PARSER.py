from bs4 import BeautifulSoup
import requests, os

NUM = "0123456789"
PRICE_TYPE = ("market_listing_price_with_fee", "market_listing_price_with_publisher_fee_only", "market_listing_price_without_fee")
PRICE_TYPE_NAME = ("с комиссией", "с комиссией к публикации", "без комиссии")

input_url = input("всатвьте ссылку:")
sticker_name = input("название стикера (необязательно):")
sticker_name = sticker_name.replace(" ", "+")

url_render = input_url+"/render/?filter="+sticker_name+"&query=&start=0&count=10&country=RU&language=russian&currency=1"
render_req = requests.get(url_render)

cnt = 54
while render_req.text[cnt] in NUM:
    cnt += 1
print("всего пушек:", render_req.text[54:cnt])

page = int(input("сколько страниц вы хотите проверить?:"))
pg = 0

while pg < page:
    print("="*10+f"\n{pg+1}-ая страница")
    url = input_url+"/?filter="+sticker_name+"&query=&start="+str(pg*10)+"&count=10&country=RU&language=russian&currency=1"
    if pg == 0:
        print("эта ссылка отправит вас на первую страницу.")
        print("-"*10)
        print(url)
        print("-"*10)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    for t in PRICE_TYPE:
        price = soup.find_all("span", class_=t)
        print(PRICE_TYPE_NAME[PRICE_TYPE.index(t)])
        for data in price:
            print(price.index(data) + 1, end = ".")
            txt = data.text[5::]
            print(txt)
    pg += 1