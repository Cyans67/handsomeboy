#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : referer_proxy.py
# @Author: Eveline Xue
# @Date  : 2019/4/28 16:33
# @Desc  :
import os
import random
import sys

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from utils.referers import referers
from utils.useragents import useragent

phantomjs_driver = r'E:\Codes\xuecode\handsomeboy\chromeDriver\phantomjs.exe'


def dynamic_load():
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    # 从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
    desired_capabilities["phantomjs.page.settings.userAgent"] = random.choice(useragent)
    # 不载入图片，爬页面速度会快很多
    # desired_capabilities["phantomjs.page.settings.loadImages"] = False
    desired_capabilities["phantomjs.page.customHeaders.Referer"] = random.choice(referers)
    # 打开带配置信息的phantomJS浏览器
    # driver = webdriver.PhantomJS(executable_path=phantomjs_driver,desired_capabilities=desired_capabilities)
    driver = webdriver.PhantomJS(executable_path=phantomjs_driver)
    driver.start_session(desired_capabilities)
    # 隐式等待5秒，可以自己调节
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    return driver, wait
