import requests
from bs4 import BeautifulSoup as BS

request = requests.get(
    "https://www.johnlewis.com/final-touch-bamboo-cutlery-set-5-piece/p4741071")
content = request.content
soup = BS(content, "html.parser")
element = soup.find("p", {"class": "price price--large",})
price = element.text.strip()

price_nosymb = float(price[1:])


if(price_nosymb > 15.00):
    print("Item is {cash}, too expensivo".format(cash = price_nosymb))
elif(price_nosymb <= 15.00 and price_nosymb >= 10):
    print("Item is {cash}, reasonable".format(cash = price_nosymb))
else:
    print("Item is {cash}, a steal".format(cash = price_nosymb))



# <span id="price_inside_buybox" class="a-size-medium a-color-price">$13.95</span>


