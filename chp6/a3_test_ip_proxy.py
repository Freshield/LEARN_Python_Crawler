# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_test_ip_proxy.py
@Time: 2021-01-20 18:04
@Last_update: 2021-01-20 18:04
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

proxies = {
    'http': 'http://127.0.0.1:12639',
    'https': 'http://127.0.0.1:12639'
}
r = requests.get('https://www.baidu.com', proxies=proxies)
print(r)
