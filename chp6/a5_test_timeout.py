# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_test_timeout.py
@Time: 2021-01-18 15:00
@Last_update: 2021-01-18 15:00
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

r = requests.get('https://www.baidu.com', timeout=1)
print(r)
r = requests.post('https://www.baidu.com', timeout=1)
print(r)