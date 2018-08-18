#!/usr/bin/env python

import requests, time, smtplib, argparse
from bs4 import BeautifulSoup

IN_STOCK_ENDPOINT = 'https://www.nike.com/launch/?s=in-stock'
UPCOMING_ENDPOINT = 'https://www.nike.com/launch/?s=upcoming'
ROOT_ENDPOINT = 'https://www.nike.com/launch/'
USER_AGENT = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' }

def scrap_snkrs():
    in_stock = requests.get(IN_STOCK_ENDPOINT, headers=USER_AGENT)
    upcoming = requests.get(UPCOMING_ENDPOINT, headers=USER_AGENT)
    root = requests.get(ROOT_ENDPOINT, headers=USER_AGENT)
    in_stock_soup = str(BeautifulSoup(in_stock.text, "lxml"))
    upcoming_soup = str(BeautifulSoup(upcoming.text, "lxml"))
    root_soup = str(BeautifulSoup(root.text, "lxml"))
    content = ''.join((in_stock_soup, upcoming_soup, root_soup))
    return content


def search_for_keywords(content, keywords, email, password, listserve):
    for keyword in keywords:
        if keyword in content:
            print('here')
            email_notification(email, password, listserve)


def email_notification(email, password, listserve):
    from_addr = email
    to_addrs = listserve
    msg = 'Subject: Snkrs Tracker Alert'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    # Print the email's contents
    print('From: ' + from_addr)
    print('To: ' + str(to_addrs))
    print('Message: ' + msg)

    # send the email
    server.sendmail(from_addr, to_addrs, msg)
    # disconnect from the server
    server.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Never catch a L again')
    parser.add_argument('-k', '--keywords', nargs="+", required=True,
                        help='Provide keywords to search for surprise sneaker drops')
    parser.add_argument('-e', '--email', help='Provide user email address', required=True)
    parser.add_argument('-p', '--password', help='Provide password for email', required=True)
    parser.add_argument('-l', '--listserve', help='Provide email addresses to send notification', nargs="+", required=True)

    args = parser.parse_args()

    web_content = scrap_snkrs()
    search_for_keywords(web_content, args.keywords, args.email, args.password, args.listserve)
