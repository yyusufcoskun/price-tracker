import requests
from bs4 import BeautifulSoup
import smtplib
from decimal import Decimal
import time

URL = 'https://www.akakce.com/fotograf-makinesi/en-ucuz-canon-eos-250d-18-55-mm-lens-dijital-slr-fotograf-makinesi-fiyati,464037219.html'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

def price_checker():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    title = soup.find('div', class_='pdt_v8').get_text()
    # print(title)

    price = soup.find('span', class_='pt_v8').get_text().strip()[0:6]
    # print(price)
    
    converted_price = Decimal(price)
    # print(converted_price)

    if(converted_price < 12.000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("mail", "pass")
    
    subject = 'PRICE DROPPED!'
    body = "Price drop:" + URL
    msg = "Subject:" +subject+'\n\n'+body
    
    server.sendmail("from","to",msg)
    
    print("Email has been sent")
    
    server.quit()
    
while (True):
    price_checker()
    time.sleep(60*60*6)