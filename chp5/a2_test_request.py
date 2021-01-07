# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_test_request.py
@Time: 2021-01-08 19:22
@Last_update: 2021-01-08 19:22
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

url = 'https://movie.douban.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': 'https://movie.douban.com/',
    'Connection': 'keep-alive'
}

req = urllib.request.Request(url, headers=headers)

html = urllib.request.urlopen(req).read().decode('utf-8')

f = open('data/a2_html.html', 'w', encoding='utf8')
f.write(html)
f.close()