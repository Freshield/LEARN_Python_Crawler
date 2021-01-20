# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_test_headers.py
@Time: 2021-01-20 18:02
@Last_update: 2021-01-20 18:02
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

headers = {
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv: 41.0) Gecko/20100101 Firefox/41.0'
}

r = requests.get('https://www.baidu.com', headers=headers)
print(r)
