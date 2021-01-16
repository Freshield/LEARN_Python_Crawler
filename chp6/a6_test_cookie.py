# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a6_test_cookie.py
@Time: 2021-01-18 15:04
@Last_update: 2021-01-18 15:04
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

temp_cookies = 'JSESSIONID_GDS=y4p7osFr_IYV5Udyd6c1drWE8MeTpQn0Y58Tg8cCONVP020y2N!450649273;name=value'
cookies_dict = dict()
for i in temp_cookies.split(';'):
    value = i.split('=')
    cookies_dict[value[0]] = value[1]

print(cookies_dict)
