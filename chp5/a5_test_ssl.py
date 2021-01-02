# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_test_ssl.py
@Time: 2021-01-08 19:49
@Last_update: 2021-01-08 19:49
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
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://kyfw.12306.cn/otn/leftTicket/init'

response = urllib.request.urlopen(url)

print(response.getcode())