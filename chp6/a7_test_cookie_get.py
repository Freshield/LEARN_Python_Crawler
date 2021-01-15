# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a7_test_cookie_get.py
@Time: 2021-01-18 15:20
@Last_update: 2021-01-18 15:20
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import requests

url = 'https://movie.douban.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': 'https://movie.douban.com/',
    'Connection': 'keep-alive'
}

r = requests.get(url, headers=headers)
print(r.cookies)
print(r)
mycookies = r.cookies

cookies_dict = requests.utils.dict_from_cookiejar(mycookies)
print(cookies_dict)

cookies_jar = requests.utils.cookiejar_from_dict(cookies_dict, cookiejar=None, overwrite=True)
print(cookies_jar)

f = open('data/cookies.txt', 'w', encoding='utf-8')
f.write(str(cookies_dict))
f.close()

f = open('data/cookies.txt', 'r')
dict_value = f.read()
f.close()

print(eval((dict_value)))
r = requests.get(url, cookies=eval(dict_value), headers=headers)
print(r.status_code)
