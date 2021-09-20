#!/usr/bin/env python# -*- coding:utf-8 -*-

from selenium import webdriver
import datetime
import time

driver = webdriver.Firefox()
# http://gate.jd.com/InitCart.aspx?pid=4993737&pcount=1&ptype=1

def login(username, password):
    driver.get("https://passport.jd.com/new/login.aspx")
    time.sleep(3)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(username)
    driver.find_element_by_name("nloginpwd").send_keys(password)
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(3)
    driver.get("https://item.jd.com/100022493730.html")
    # there is test link -> https://item.jd.com/100013381490.html
    time.sleep(3)
    # driver.find_element_by_link_text("去结算").click()
    now = datetime.datetime.now()
    #now_time = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print('login success, you can ou up!')
def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()

        if driver.find_element_by_link_text("加入购物车").click() == 1:
        # if driver.find_element_by_xpath("//*/ul[@class='nav_item']/li[text()='加入购物车']").click() == 1:  #this is another way.
               print('There is ur Xbox Series S coming!')

        # if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
        #     driver.find_element_by_id('order-submit').click()
        #     time.sleep(3)
        #     print(now.strftime('%Y-%m-%d %H:%M:%S'))
        #     print('purchase success')
        # time.sleep(0.5)
login('your_jd_username', 'your_jd_password')
buy_on_time('2017-11-28 10:00:00')
