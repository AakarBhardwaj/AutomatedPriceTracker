import requests
from bs4 import BeautifulSoup
import smtplib
import time

def check_price():
    URL='https://www.flipkart.com/apple-iphone-xr-black-128-gb/p/itmf9z7zhdgzwmzm?pid=MOBF9Z7ZYWNFGZUC&lid=LSTMOBF9Z7ZYWNFGZUCEOHXKN&marketplace=FLIPKART&srno=b_1_2&otracker=undefined_footer_footer&fm=organic&iid=2658da97-b6a9-43bc-bc3f-f5551612af63.MOBF9Z7ZYWNFGZUC.SEARCH&ssid=col0uopao00000001603795606510'
    headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    price=float(soup.find(class_="_1vC4OE _3qQ9m1").get_text().strip()[1::].replace(",",""))
    print(price)
    if price<50000.0:
        send_mail()

def send_mail():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("aakarbhardwaj7@gmail.com",'vlnbafilsuclwwyv')
    subject="Price fell down!"
    body="Check out the Flipkart link https://www.flipkart.com/apple-iphone-xr-black-128-gb/p/itmf9z7zhdgzwmzm?pid=MOBF9Z7ZYWNFGZUC&lid=LSTMOBF9Z7ZYWNFGZUCEOHXKN&marketplace=FLIPKART&srno=b_1_2&otracker=undefined_footer_footer&fm=organic&iid=2658da97-b6a9-43bc-bc3f-f5551612af63.MOBF9Z7ZYWNFGZUC.SEARCH&ssid=col0uopao00000001603795606510"
    msg=f'Subject:{subject}\n\n{body}'
    server.sendmail('aakarbhardwaj7@gmail.com','aakarbhardwaj7@gmail.com',msg)
    print("Email has been sent!")
    server.quit()
while(True):
    check_price()
    time.sleep(60*60)