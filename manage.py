import sys
import time
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# 声明浏览器对象，将chromedriver驱动放在chrome浏览器安装目录下，指定驱动的绝对路径
browser = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\google\Chrome\Application\chromedriver')


# 请朋友们先进入该网站注册账号密码
id = ''
key = ''

runtime = 300

# 1.打开浏览器，输入网址
browser.maximize_window() # 浏览器最大化
browser.get('http://gy.com/admin/weChat/material/detail?id=0&project_id=4')
browser.implicitly_wait(30) # 加入隐式等待，防止崩溃

# 2.寻找"点击登录"节点
button = browser.find_element_by_xpath("//button[@class='ant-btn submit___Q43EO ant-btn-primary ant-btn-lg']")
browser.execute_script("arguments[0].click();", button)

# 3.寻找"账号登录在这里"
# button2 = browser.find_element_by_xpath("//div[@class='login-switch-btn']")
# browser.execute_script("arguments[0].click();", button2)

# 4.寻找“账号输入框”
input_id = browser.find_element_by_xpath("//input[@placeholder='手机号']")
input_id.send_keys(id)

# 5.寻找“密码输入框”
input_key = browser.find_element_by_xpath("//input[@placeholder='密码']")
input_key.send_keys(key)

# 6.寻找"点击登录"节点
button3 = browser.find_element_by_xpath("//button[@type='submit']")
browser.execute_script("arguments[0].click();", button3)

#7.获取a标签为图片的内容
us = browser.find_elements_by_xpath(".//a[@class='ant-dropdown-link ant-dropdown-trigger']")
list = []
count = 1
action = ActionChains(browser)
sleep(5)

imgs = browser.find_elements_by_xpath("//img")
for img in imgs:
    src = img.get_attribute('src')
    reponse = requests.get(src)
    name = 'fengexian'+str(count)
    # name = 'd:/photo.jpg'
    with open(f'D:\work(python)\Redis-\images\{name}.gif', 'wb') as ft:
        ft.write(reponse.content)
    count +=1
    sleep(1)
    print(src)
sys.exit()











