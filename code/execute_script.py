# -----encoding:utf8-----
import random

import requests

from utils.referers import referers
from utils.urls import urls
from utils.useragents import useragent
from  selenium import webdriver

def get_rp(url):
    header = {
        'user-agent': random.choice(useragent),
        'referer': random.choice(referers)
    }
    rq = requests.get(url, headers=header)
    print(rq.text)


if __name__ == '__main__':
    for url in urls:
        # 浏览器响应
        get_rp(url)
        # webdriver.Chrome
