# -*- coding: utf-8 -*-

import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver import ActionChains

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("disable-infobars")


# 账号与密码
Account = ["meiruiTF", "cdjianli","bjykyl"]
Password = ["cdmeirui123","cdjianli123","ykyl180225"]

# 伪装浏览器头
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "e.dianping.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

# 目标网址
target = r"https://epassport.meituan.com/account/unitivelogin?bg_source=2&service=dpmerchantlogin&feconfig=dpmerchantlogin&leftBottomLink=https://e.dianping.com/shopaccount%2fphoneRegisterAccount&continue=https%3A%2F%2Fe.dianping.com%2Fshopaccount%2Flogin%2Fsetedper%3FtargetUrl%3Dhttps%253A%252F%252Fe.dianping.com%252Fshopportal%252Fpc%252Fnewindex"

# 登陆后的session（）
IndexResponse = requests.session()

# 备用字典
DataInfo = {'status_code':'','headers':'' ,'html_code':''}

# 错误信息
ErrorInfo = "connect error, code is = "

# session登陆商家后台模块，动态cookies

# 请求商家后台，并提供相应返回值
def get_account(target, header): #请求商家后台
    try:
        ChromeBrowser = webdriver.Chrome(options=ChromeOptions)
        RowAction = ActionChains(ChromeBrowser)
        ChromeBrowser.get(target)
        time.sleep(0.3)
        ChromeBrowser.find_element_by_xpath('//*[@id="login"]').send_keys(Account[1])
        ChromeBrowser.find_element_by_xpath('//*[@id="password"]').send_keys(Password[1])
        ChromeBrowser.find_element_by_xpath('//*[@id="login-form"]/button').submit()
        time.sleep(0.5)
        if ChromeBrowser.find_element_by_xpath('//*[@id="yodaBox"]'):
            ScrollBar = ChromeBrowser.find_element_by_xpath('//*[@id="yodaBox"]')
            RowAction.click_and_hold(ScrollBar)
            for i in range(0,198):
                if i != 197:
                    RowAction.move_by_offset(i,0)
                else:
                    RowAction.release()
            RowAction.perform()
        time.sleep(1)
        Cookies = ChromeBrowser.get_cookies()
        for CookiesInfo in Cookies:
            IndexResponse.cookies.set(CookiesInfo['name'], CookiesInfo['value'])
        return IndexResponse
    except Exception as errorinfo:
        return errorinfo

# 主函数
if __name__ == "__main__": #主函数
    res = get_account(target, header)
    
