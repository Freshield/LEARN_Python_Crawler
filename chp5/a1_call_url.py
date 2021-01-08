# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_call_url.py
@Time: 2020-01-07 19:15
@Last_update: 2020-01-07 19:15
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

response = urllib.request.urlopen('http://www.baidu.com/', None, 2)

html = response.read().decode('utf8')

f = open('data/html.txt', 'w', encoding='utf8')
f.write(html)
f.close()