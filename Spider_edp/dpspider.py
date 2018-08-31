# -*- coding: utf-8 -*-

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from Spider_edp.datachange import MeChart_Optimization, DataOptimization

# 浏览器设置
ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("disable-infobars")

# 账号与密码
accountdic = {
    'meiruitf': ['MeiruiTF', 'cdmeirui123', '8352512'],
    'cdjianli': ['cdjianli', 'cdjianli123', '']
}

# 报表数据字典
resultList = []

Account = ["meiruiTF", "cdjianli", "bjykyl", "cicheng"]
Password = ["cdmeirui123", "cdjianli123", "ykyl180225", "71815igm"]

# 伪装浏览器头
header = {
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "zh-CN,zh;q=0.9",
    "Connection":
    "keep-alive",
    "Host":
    "e.dianping.com",
    "Referer":
    "http://e.dianping.com/mda/web/traffic",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

# 流量数据接口
TrafficScale = '''
http://e.dianping.com/mda/v2/traffic/scale?platformType=0&dateType=30&source=1&shopId=8352512&tab=0&device=1
'''

# 流量质量接口
TrafiicQuality = 'http://e.dianping.com/mda/v2/traffic/quality?platformType=0&dateType=30&source=1&shopId=8352512&tab=1&device=1'

# 口碑管理接口
MerChat_api = 'https://m.dianping.com/merchant/im/user/search?pageNum=1&pageSize=1000'

# 登陆后的session（）
IndexResponse = requests.session()


# session登陆商家后台模块，动态cookies
# 请求商家后台，并提供相应返回 session()
def Get_CookeandSession(target):  # 请求商 家后台
    try:
        ChromeBrowser = webdriver.Chrome(options=ChromeOptions)
        RowAction = ActionChains(ChromeBrowser)
        ChromeBrowser.get(target)
        ChromeBrowser.switch_to.frame(0)
        WebDriverWait(ChromeBrowser, 5).until(
            lambda ChromeBrowser: ChromeBrowser.find_elements_by_xpath(
                '//*[@id="login"]')
        )
        ChromeBrowser.find_element_by_xpath(
            '//*[@id="login"]').click()
        ChromeBrowser.find_element_by_xpath(
            '//*[@id="login"]').send_keys(
            Account[0])
        ChromeBrowser.find_element_by_xpath(
            '//*[@id="password"]').click()
        ChromeBrowser.find_element_by_xpath(
            '//*[@id="password"]').send_keys(
            Password[0])
        ChromeBrowser.find_element_by_xpath(
            '//*[@id="login-form"]/button').click()
        WebDriverWait(ChromeBrowser, 5).until(
            lambda ChromeBrowser: ChromeBrowser.find_element_by_xpath(
                '//*[@id="yodaBox"]'
                )
        )
        ScrollBar = ChromeBrowser.find_element_by_xpath('//*[@id="yodaBox"]')
        RowAction.click_and_hold(ScrollBar)
        for i in range(0, 198):
            if i != 197:
                RowAction.move_by_offset(i, 0)
            else:
                RowAction.move_by_offset(i, 0)
                RowAction.release()
        RowAction.perform()
        WebDriverWait(ChromeBrowser, 10).until(
            lambda ChromeBrowser: ChromeBrowser.find_element_by_xpath(
                '/html/body/div[2]/div/div[1]/div[4]/div/div[2]/ul/li[3]'
                )
        ).click()
        IndexCookies = ChromeBrowser.get_cookies()
        for Cookies in IndexCookies:
            IndexResponse.cookies.set(Cookies['name'], Cookies['value'])
        return IndexResponse
    except Exception as errorinfo:
        return errorinfo


# 获取网页结构
def Get_Data(targeturl, res):
    result = res.get(targeturl)
    return result.text


# 获取带cookies的session对象
def get_res(IndexCookies):
    for Cookies in IndexCookies:
        IndexResponse.cookies.set(Cookies['name'], Cookies['value'])
    return IndexResponse


# 获取流量
def Getflowdata(res):  # 主函数
    ScaleResponse = Get_Data(TrafficScale, res)
    QualityResponse = Get_Data(TrafiicQuality, res)
    TrafficDatas = DataOptimization(ScaleResponse, QualityResponse)
    return TrafficDatas


# 获取口碑
def Getchatdata(res):
    MerChatResponse = Get_Data(MerChat_api, res)
    MerchatDatas = MeChart_Optimization(MerChatResponse)
    return MerchatDatas
