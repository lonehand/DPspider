# -*- coding: utf-8 -*-
import datetime
import re
import time

import arrow
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from Spider_edp.datachange import AppointMent_Optimization
from Spider_edp.datachange import DataOptimization
from Spider_edp.datachange import MeChart_Optimization
from Spider_edp.datachange import SaleOnline_Optimaization


# 浏览器设置
ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("disable-infobars")

# 账号与密码
accountdic = {
    'meiruitf': ['MeiruiTF', 'cdmeirui123', '8352512'],
    'cdjianli': ['cdjianli', 'cdjianli123', '']
}

# 报表数据字典
Appointresult = []
Appintdict = {}

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
http://e.dianping.com/mda/v2/traffic/scale?platformType=0&dateType=30&source=1&shopId=73082729&tab=0&device=1
'''

# 流量质量接口
TrafiicQuality = 'http://e.dianping.com/mda/v2/traffic/quality?platformType=0&dateType=30&source=1&shopId=73082729&tab=1&device=1'

# 口碑管理接口
MerChat_api = r'https://m.dianping.com/merchant/im/user/search?pageNum=1&pageSize=1000'

# 订单中心接口
appointment_api = 'https://e.dianping.com/e-beauty/book/ajax/ajaxOrderList?display=2&shopId=73082729&page=%s'

# 线上销售数据（一个月+目前）
SaleOnline_api = 'https://e.dianping.com/ktv/dzbook/trade/api/queryorderlist.wbc?&beginTime=%s&endTime=%s&page=1&pageSize=1000&queryType=3&bizname=medicalbeautyprepay'

# 登陆后的session（）
IndexResponse = requests.session()


# session登陆商家后台模块，动态cookies
# 请求商家后台，并提供相应返回 session()pI
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
            Account[1])
        ChromeBrowser.find_element_by_xpath(
            '//*[@id="password"]').click()
        ChromeBrowser.find_element_by_xpath(
            '//*[@id="password"]').send_keys(
            Password[1])
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


# 获取预约网页结构
def Get_appiont_Data(targeturl, res, page):
    result = res.get(targeturl % page)
    return result.text


# 获取带cookies的session对象
def get_res(IndexCookies):
    for Cookies in IndexCookies:
        IndexResponse.cookies.set(Cookies['name'], Cookies['value'])
    return IndexResponse


# 获取预约最大页数
def get_maxpage(htmltree):
    max_page = re.search('"pageCount":(.*?),"pageSize"', htmltree).group(1)
    return max_page


# =======================获取流量==================================
def Getflowdata(res):  # 主函数
    ScaleResponse = Get_Data(TrafficScale, res)
    QualityResponse = Get_Data(TrafiicQuality, res)
    TrafficDatas = DataOptimization(ScaleResponse, QualityResponse)
    return TrafficDatas


# ========================获取口碑================================
def Getchatdata(res):
    MerChatResponse = Get_Data(MerChat_api, res)
    MerchatDatas = MeChart_Optimization(MerChatResponse)
    return MerchatDatas


# ======================预约数据 放慢一秒===========================
def Get_appdatalist(data):
    result = []
    addtime = re.search(
        '"addTime":"(.*?)","arriveStatus"', data
        ).group(1).replace('T', ' ')
    userfrom = re.search(
        '"orderSourceVal":"(.*?)","orderTime"', data
        ).group(1)
    usernick = re.search(
        '"customerName":"(.*?)","merchantComment', data
        ).group(1)
    phone = re.search(
        'phoneNo":"(.*?)","productId', data
        ).group(1)
    comment = re.search(
        'comment":"(.*?)","count"', data
        ).group(1)
    status = re.search(
        '"arriveStatusVal":"(.*?)","comment"', data
        ).group(1)
    year = addtime[:10]
    clock = addtime[11:19]
    result.append(int(year[:4]))
    result.append(int(year[5:7]))
    result.append(year)
    result.append(clock)
    result.append(str(userfrom))
    result.append(str(usernick))
    result.append(str(phone))
    if comment != '':
        result.append((comment))
    else:
        result.append('无')
    result.append(status)
    return result


# ==========================预约中心==================================
def GetAppointresult(res):
    page = 1
    num = 2
    Appintdict = {}
    AppointMenttree = Get_appiont_Data(appointment_api, res, page)
    MaxPage = int(get_maxpage(AppointMenttree))
    for page in range(1, MaxPage + 1):
        time.sleep(1)
        Appointtree = Get_appiont_Data(appointment_api, res, str(page))
        AppointData = AppointMent_Optimization(Appointtree)
        for data in AppointData:
            Ddata = Get_appdatalist(data)
            Appintdict[num] = Ddata
            num += 1
    return Appintdict


# ========================线上订单数据================================
def Get_YesterMonth(today):
    return datetime.date(
        today.year - (today.month == 1), today.month - 1 or 12, 1
        )


# 开始与结束日期的13位时间戳
def GetStartandEndDate():
    today = datetime.datetime.today()
    YesterMonth = Get_YesterMonth(today)
    starttime = YesterMonth.strftime("%Y-%m-%d %H:%M:%S")
    endtime = today.strftime("%Y-%m-%d %H:%M:%S")[:10]+" 00:00:00"
    starttime = time.strptime(starttime, '%Y-%m-%d %H:%M:%S')
    endtime = time.strptime(endtime, '%Y-%m-%d %H:%M:%S')
    starttime = arrow.get(starttime).timestamp*1000
    endtime = arrow.get(endtime).timestamp*1000
    return starttime, endtime


# 获取HtmlTree
def Get_SaleTree(res, starttime, endtime):
    result = res.get(SaleOnline_api % (str(starttime), str(endtime)))
    return result.text


# 加工返回字典
def GetSaleOnlineresult(res):
    starttime, endtime = GetStartandEndDate()
    SaleOnlinetree = Get_SaleTree(res, starttime, endtime)
    SaleOnlineData = SaleOnline_Optimaization(SaleOnlinetree)

