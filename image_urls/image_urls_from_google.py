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

import json

def main():
    args = sys.argv
    url = 'https://www.google.co.jp/search?tbm=isch&q='+args[1]
    regex = r'[^\x00-\x7F]'
    matchedList = re.findall(regex,url)
    for m in matchedList:
        url = url.replace(m, urllib.parse.quote_plus(m, encoding="utf-8"))

    #print(url)

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
    }

    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    body = response.read()

    #print(body)

    # HTML をパースする
    soup = BeautifulSoup(body, "lxml")

    div_tags = soup.find_all('div', {'class': 'rg_meta'})
    for div_tag in div_tags:
        j = json.loads(div_tag.text)
        print(j["ou"])

if __name__ == '__main__':
    main()