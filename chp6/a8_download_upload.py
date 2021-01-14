# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a8_download_upload.py
@Time: 2021-01-18 15:43
@Last_update: 2021-01-18 15:43
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

url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1275774655,4144136426&fm=26&gp=0.jpg'
r = requests.get(url)
f = open('data/test.jpg', 'wb')
f.write(r.content)
f.close()
