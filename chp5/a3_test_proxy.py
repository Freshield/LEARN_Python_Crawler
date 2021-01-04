# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_test_proxy.py
@Time: 2021-01-08 19:31
@Last_update: 2021-01-08 19:31
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

url = 'http://movie.douban.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': 'https://movie.douban.com/',
    'Connection': 'keep-alive'
}

proxy_handler = urllib.request.ProxyHandler({
    'http': '127.0.0.1:12639',
    'https': '127.0.0.1:12639'
})

opener = urllib.request.build_opener(proxy_handler)

request = urllib.request.Request(url, headers=headers)

response = opener.open(request)

html = response.read().decode('utf-8')

f = open('data/a3_html2.html', 'w', encoding='utf8')
f.write(html)
f.close()