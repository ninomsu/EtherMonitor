import urllib.request as ur
import re
import time
import smtplib
count = 0
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( 'Your Email', 'Your Password' )
lastHourPrice = 100.0;

while(True):
    response = ur.urlopen( "https://coinmarketcap.com/currencies/ethereum/")
    html = response.read()
    regex = '<span class="text-large" id="quote_price">(.+?)</span>'
    pattern = re.compile(regex)
    price =re.findall(pattern, html.decode('utf-8'))
    priceNum = float(price[0][1:])
    test = ""
    
    #if the price of ether decreases by a min of 10% in the last hour, send text
    if priceNum < lastHourPrice:
            if (1.0 - (priceNum/lastHourPrice)) >= .01:
                message = "Price of Ether = " + price[0] + "\n" + "Ether dropped " + str(round(100*(1.0 - (priceNum/lastHourPrice)), 2)) + "%"
                server.sendmail( 'YOUREMAIL', 'YOURPHONENUMBER@mms.att.net', message )

    #if the price of ether increases by a min of 10% in the last hour, send text    
    else:
        if (((priceNum - lastHourPrice)/lastHourPrice)) >= .01:
                message = "Price of Ether = " + price[0] + "\n" + "Ether went up " + str(round(100*(((priceNum - lastHourPrice)/lastHourPrice)), 2)) + "%"
                server.sendmail( 'YOUREMAIL', 'YOURPHONENUMBER@mms.att.net', message )
        

    #hour goes by, set last hour value
    lastHourPrice = priceNum;

    #sleep for hour
    time.sleep(3600)

