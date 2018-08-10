# -*- coding: utf-8 -*-

import requests
import random
from bs4 import BeautifulSoup
import json
import datetime

# 伪装浏览器头
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": r"_lxsdk_cuid=1651dbc8f58c8-036d4b7b2984bd-9393265-1fa400-1651dbc8f59c8; _lxsdk=1651dbc8f58c8-036d4b7b2984bd-9393265-1fa400-1651dbc8f59c8; _hc.v=\cc1d08d6-9c75-4b66-bacd-ba60e886bcf4.1533802221\; _lxsdk_s=165217310bc-f80-f7e-808%7C%7C8",
    "Host": "e.dianping.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}


# 目标网址
target = "http://e.dianping.com"

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
        res = requests.get(target, headers=header)
        if res.status_code == 200:
            return res.text
        else:
            return ErrorInfo+res.status_code
    except Exception as errorinfo:
        return errorinfo

# 主函数
if __name__ == "__main__": #主函数
    Webdata = get_account(target, header)
    print(Webdata)