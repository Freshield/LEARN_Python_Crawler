# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_test_call.py
@Time: 2021-01-20 17:40
@Last_update: 2021-01-20 17:40
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
import json

url = 'https://www.baidu.com'
url = 'http://www.baidu.com/s?wd=python'

r = requests.get(url)

print(r.url)
print(r.text)

url = 'http://www.baidu.com/s'
params = {'wd': 'python'}
r = requests.get(url, params=params)
print(r.text)
print(r.url)

data = {'key1': 'value1', 'key2': 'value2'}
data = json.dumps(data)
r = requests.post('https://www.baidu.com', data=data)
print(r.text)
print(r)