#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File  : selenium_test.py
@Author: Eveline Xue
@Date  : 2019/4/28 13:50
@Desc  : 使用selenium自动化测试工具模拟浏览器点击
'''
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from referer_proxy import dynamic_load
from utils.referers import referers
from utils.useragents import useragent

EXECUTE_PATH = r'C:\Users\22\PycharmProjects\handsomeboy\chromeDriver\chromedriver74.exe'


# 90
def search(query_url):
    browser, wait = dynamic_load()
    browser.get(query_url)
    browser.implicitly_wait(10)
    print(browser.page_source)
    try:
        wait.until(
            EC.presence_of_all_elements_located((By.LINK_TEXT, '普通下载'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="go"]/a[4]/span')))
    except:
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tt_6"]/a[1]')))
    submit.click()
    time.sleep(20)
    url = 'https://httpbin.org/headers'
    browser.execute_script('window.location.href = "{}";'.format(url))
    wait.until(lambda driver: driver.current_url == url)
    print(browser.page_source)
    browser.quit()


def get_exploer():
    # 加表头
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent={}'.format(random.choice(useragent)))
    browser = webdriver.Chrome(executable_path=EXECUTE_PATH, options=options)
    wait = WebDriverWait(browser, 10)
    return browser, wait


def main():
    search('http://www.90pan.com/b1173540')


if __name__ == '__main__':
    main()
