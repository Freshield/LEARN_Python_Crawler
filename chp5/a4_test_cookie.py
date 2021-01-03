# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_test_cookie.py
@Time: 2021-01-08 19:40
@Last_update: 2021-01-08 19:40
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
from http import cookiejar

filename = 'data/cookie2.txt'

cookie = cookiejar.MozillaCookieJar(filename)
# cookie = cookiejar.MozillaCookieJar()
# cookie.load(filename)

handler = urllib.request.HTTPCookieProcessor(cookie)

url = 'https://movie.douban.com/'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': 'https://movie.douban.com/',
    'Connection': 'keep-alive'
}

opener = urllib.request.build_opener(handler)

request = urllib.request.Request(url, headers=headers)

response = opener.open(request)

cookie.save(ignore_discard=True, ignore_expires=True)
# print(cookie)