#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # Python 3
    from urllib import request
except ImportError:
    # Python 2
    import urllib2 as request

import sys
from bs4 import BeautifulSoup

import re
from urllib.parse import urlparse
import urllib.request

def main():
    args = sys.argv
    url = 'https://www.bing.com/images/search?q='+args[1]
    regex = r'[^\x00-\x7F]'
    matchedList = re.findall(regex,url)
    for m in matchedList:
        url = url.replace(m, urllib.parse.quote_plus(m, encoding="utf-8"))

    response = request.urlopen(url)
    body = response.read()

    #print(body)

    # HTML をパースする
    soup = BeautifulSoup(body, "lxml")

    a_tags = soup.find_all('a', {'class': 'thumb'})
    for a_tag in a_tags:
        print(a_tag['href'])

if __name__ == '__main__':
    main()