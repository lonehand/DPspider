# -*- coding: utf-8 -*-

import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver.support.ui as ui


# 账号与密码
Account = ["TFmeirui", "cdjianli","bjykyl"]
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

# 登陆账号
post_data = {
    "login" : "MeiruiTF",
    "loginTyoe" : "account",
    "password" : "cdmeirui123",
}

# 目标网址
target1 = "http://e.dianping.com/slogin"
target2 = "https://e.dianping.com/shopaccount/login/setedper?targetUrl=https://e.dianping.com/shopportal/newindex"
target3 = "https://e.dianping.com/shopportal/newindex"

# 备用字典
DataInfo = {'status_code':'','headers':'' ,'html_code':''}

# 错误信息
ErrorInfo = "connect error, code is = "

# session登陆商家后台模块，动态cookies
def login(self,posturl,postdata):
    '''
    self.build_opener()
    postdata = urllib.urlencode(postdata)
    request = urllib2.Request(url=posturl,data=postdata,headers=self.headers)
    #print self.opener.open(request)
    resp = urllib2.urlopen(request).read()
    print resp
    '''
    self.session = requests.Session()
    r = self.session.post(posturl,data=postdata,headers=self.headers)
    return dict(r.cookies) if not isinstance(r.cookies,dict) else r.cookies

# 请求商家后台，并提供相应返回值
def get_account(target, header): #请求商家后台
    try:
        ChromeBrowser = webdriver.Chrome()
        ChromeBrowser.get(target)
        wait = ui.WebDriverWait
        ChromeBrowser.find_element_by_xpath('//*[@id="login"]//div[2]').send_keys(Account[0])
        ChromeBrowser.find_element_by_xpath('//*[@id="password"]//div[2]').send_keys(Password[0])
        ChromeBrowser.find_element_by_xpath('//*[@id="login-form"]/button').submit()
    except Exception as errorinfo:
        return errorinfo

# 主函数
if __name__ == "__main__": #主函数
    Webdata = get_account(target1, header)
    print(Webdata)
