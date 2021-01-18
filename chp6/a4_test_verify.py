# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_test_verify.py
@Time: 2021-01-20 18:06
@Last_update: 2021-01-20 18:06
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

url = 'https://kyfw.12306.cn/otn/leftTicket/init'

r = requests.get(url, verify=False)

print(r)

r = requests.get(url, verify=True)

print(r)
