# -*- coding: utf-8 -*-
import json
import time

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from datachange import DataOptimization

# 浏览器设置
ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("disable-infobars")

# 账号与密码
Account = ["meiruiTF", "cdjianli", "bjykyl"]
Password = ["cdmeirui123", "cdjianli123", "ykyl180225"]

# 伪装浏览器头
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "e.dianping.com",
    "Referer": "http://e.dianping.com/mda/web/traffic",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

# 登陆网址
LoginUrl = ('https://epassport.meituan.com/account/unitivelogin?bg_source=2&service=dpmerchantlogin&feconfig=dpmerchantlogin&leftBottomLink='
            'https://e.dianping.com/shopaccount%2fphoneRegisterAccount&continue='
            'https%3A%2F%2Fe.dianping.com%2Fshopaccount%2Flogin%2Fsetedper%3FtargetUrl%3D'
            'https%253A%252F%252Fe.dianping.com%252Fshopportal%252Fpc%252Fnewindex')

# 流量数据接口
TargetUrl = "http://e.dianping.com/mda/v2/traffic/scale?platformType=0&dateType=30&source=1&shopId=8352512&tab=0&device=1"

# 登陆后的session（）
IndexResponse = requests.session()

# session登陆商家后台模块，动态cookies
# 请求商家后台，并提供相应返回 session()
def Get_CookeandSession(target):  # 请求商家后台
    try:
        ChromeBrowser = webdriver.Chrome(options=ChromeOptions)
        RowAction = ActionChains(ChromeBrowser)
        ChromeBrowser.get(target)
        WebDriverWait(ChromeBrowser,10).until(lambda ChromeBrowser: ChromeBrowser.find_elements_by_xpath('//*[@id="login"]'))
        ChromeBrowser.find_element_by_xpath(
            '//*[@id="login"]').send_keys(Account[0])
        ChromeBrowser.find_element_by_xpath(
            '//*[@id="password"]').send_keys(Password[0])
        ChromeBrowser.find_element_by_xpath(
            '//*[@id="login-form"]/button').submit()
        WebDriverWait(ChromeBrowser, 10).until(lambda ChromeBrowser: ChromeBrowser.find_element_by_xpath('//*[@id="yodaBox"]'))
        ScrollBar = ChromeBrowser.find_element_by_xpath(
            '//*[@id="yodaBox"]')
        RowAction.click_and_hold(ScrollBar)
        for i in range(0, 198):
            if i != 197:
                RowAction.move_by_offset(i, 0)
            else:
                RowAction.release()
        RowAction.perform()
        WebDriverWait(ChromeBrowser, 10).until(lambda ChromeBrowser: ChromeBrowser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[4]/div/div[2]/ul/li[3]')).click()
        IndexCookies = ChromeBrowser.get_cookies()
        return IndexCookies
    except Exception as errorinfo:
        return errorinfo

# 获取流量
def Get_Data(TargetUrl, IndexCookies):
    for Cookies in IndexCookies:
        IndexResponse.cookies.set(
            Cookies['name'], Cookies['value']
        )
    IndexResponse.headers.clear()
    result = IndexResponse.get(TargetUrl)
    return result.text

# 主函数
if __name__ == "__main__":  # 主函数

    '''
        __author__: johnny leaf
    '''

    IndexCookies = Get_CookeandSession(LoginUrl)
    Response = Get_Data(TargetUrl, IndexCookies)
    print(Response)
    a = DataOptimization(Response)





