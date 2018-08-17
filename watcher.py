#!/usr/bin/env python

import requests, time, smtplib
from bs4 import BeautifulSoup

IN_STOCK_URL = 'https://www.nike.com/launch/?s=in-stock'
UPCOMING_URL = 'https://www.nike.com/launch/?s=upcoming'
ROOT_URL = 'https://www.nike.com/launch/'

while True:
    agent = { "User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' }
    in_stock = requests.get(IN_STOCK_URL, headers=agent)
    upcoming = requests.get(UPCOMING_URL, headers=agent)
    root = requests.get(ROOT_URL, headers=agent)
    # parse the downloaded homepage and grab all text, then,
    in_stock_soup = BeautifulSoup(in_stock.text, "lxml")
    upcoming_soup = BeautifulSoup(upcoming.text, "lxml")
    root_soup = BeautifulSoup(root.text, "lxml")
    # if the number of times the word "Google" occurs on the page is less than 1,
    if str(in_stock_soup).find("") == -1 & str(upcoming_soup).find("") == -1 & str(root_soup).find("") == -1:
        # wait 60 seconds,
        time.sleep(60)
        print('sleeping')
        # continue with the script,
        continue

    else:
        # create an email message with just a subject line,
        msg = 'Subject: Snkr Tracker Alert'
        # set the 'from' address,
        fromaddr = ''
        # set the 'to' addresses,
        toaddrs  = ['']

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login('', '')

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()

        break
