import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from telegram_bot import send_msg

my_url = 'https://www.bug.co.il/brand/ps5/ps5/console/blue/ray'
# open connection, grab the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html parsing
page_soup = soup(page_html, "html.parser")

no_stock = page_soup.findAll("span",{"class":"product-page-no-inventory"})
yes_stock = page_soup.findAll("span",{"onclick":"addToCart(this,14074);return false;"})
stock_parent = page_soup.findAll("div",{"class":"span_6_of_12 col float-right-col"})

#Send a telegram message
if len(no_stock) != 1:
    send_msg("IN STOCK !!!")
    send_msg("https://www.bug.co.il/brand/ps5/ps5/console/blue/ray")
    print("in stock")
