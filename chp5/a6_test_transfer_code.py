# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a6_test_transfer_code.py
@Time: 2021-01-08 20:06
@Last_update: 2021-01-08 20:06
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import urllib.request
import urllib.parse

url = 'https://movie.douban.com/'

data = {
    'value': 'true',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': 'https://movie.douban.com/',
    'Connection': 'keep-alive'
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url, headers=headers)

req = urllib.request.urlopen(request, data=data)
print(req)

html = req.read().decode('utf-8')

f = open('data/a6_html.html', 'w', encoding='utf8')
f.write(html)
f.close()

url = '%2523%25E7%25BC%2596%25E7%25A8%258B%2523'

first = urllib.parse.unquote(url)
print(first)

second = urllib.parse.unquote(first)
print(second)