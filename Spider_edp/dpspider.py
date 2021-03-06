# -*- coding: utf-8 -*-
import datetime
import re
import time

import requests
import json
from lxml import etree
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from Spider_edp.datachange import AppointMent_Optimization
from Spider_edp.datachange import DataOptimization
from Spider_edp.datachange import MeChart_Optimization
from Spider_edp.datachange import SaleOnline_Optimaization
from Spider_edp.datachange import Commment_Optimaization


# 浏览器设置
ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("disable-infobars")
# 报表数据字典
Appointresult = []
Appintdict = {}

Account = [
    "meiruiTF", "cdjianli", "bjykyl", "cicheng", 'tongyan88888',
    'fenghuangyimei', 'tjsgzx520', 'ieshan23', 'HX73357653', 'deermeike',
    'mtzyyzx'
]
Password = [
    "cdmeirui123", "cdjianli123", "ykyl180225", "71815igm", 'tongyan61',
    'fhymfh1234', 'tjsgzx2015', '37878jmd', '65787488', '30826rpo', 'meitan666'
]

# 伪装浏览器头
header = {
    "Accept":
    "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "zh-CN,zh;q=0.9",
    "Connection":
    "keep-alive",
    "Content-Type":
    "application/x-www-form-urlencoded; charset=UTF-8",
    "Host":
    "e.dianping.com",
    "Origin":
    "https://e.dianping.com",
    "Referer":
    "https://e.dianping.com/comment/shopreviews/list",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "X-Requested-With":
    "XMLHttpRequest"
}

# 流量数据接口
TrafficScale = '''
http://e.dianping.com/mda/v2/traffic/scale?platformType=0&dateType=30&source=1&shopId=%s&tab=0&device=1
'''

# 流量质量接口
TrafiicQuality = '''
http://e.dianping.com/mda/v2/traffic/quality?platformType=0&dateType=30&source=1&shopId=%s&tab=1&device=1
'''

# 咨询数据接口
MerChat_api = '''
https://m.dianping.com/merchant/im/user/search?pageNum=1&pageSize=1000&fromLastContact=%s&toLastContact=%s&shopId=s%s
'''

# 预约数据接口
appointment_api = '''
https://e.dianping.com/e-beauty/book/ajax/ajaxOrderList?shopId=%s&status=0&datetime=%s%%2C%s&phoneNo=&orderSource=0&page=%s&display=2
'''

# 线上销售数据（一个月+目前）
SaleOnline_html = '''
https://e.dianping.com/receiptreport/tuangouConsumeDetail?page=%s&selectedBeginDate=%s%%2000:00:00&selectedEndDate=%s%%2000:00:00
'''

# 体验报告数据接口（post）
Comment_api = "https://e.dianping.com/comment/shopreviews/shopreviewlist"

# 登陆后的session（）
IndexResponse = requests.session()


# session登陆商家后台模块，动态cookies
# 请求商家后台，并提供相应返回 session()pI
def Get_CookeandSession(target, acountlist):  # 请求商 家后台
    try:
        ChromeBrowser = webdriver.Chrome(options=ChromeOptions)
        RowAction = ActionChains(ChromeBrowser)
        ChromeBrowser.get(target)
        ChromeBrowser.switch_to.frame(0)
        WebDriverWait(ChromeBrowser, 5).until(
            lambda ChromeBrowser: ChromeBrowser.find_elements_by_xpath(
                '//*[@id="login"]'
                )
        )
        ChromeBrowser.find_element_by_xpath('//*[@id="login"]').click()
        ChromeBrowser.find_element_by_xpath('//*[@id="login"]').send_keys(
            acountlist[0])
        ChromeBrowser.find_element_by_xpath('//*[@id="password"]').click()
        ChromeBrowser.find_element_by_xpath('//*[@id="password"]').send_keys(
            acountlist[1])
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
        ChromeBrowser.quit()
        return IndexResponse
    except Exception as errorinfo:
        return errorinfo


# 获取网页结构
def Get_Data(targeturl, res, acountlist):
    result = res.get(targeturl % acountlist[2])
    return result.text


# 获取预约网页结构
def Get_appiont_Data(targeturl, res, page, acountlist):
    starttime = '1537200000000'
    endtime = '1533052800000'
    result = res.get(targeturl % (acountlist[2], endtime, starttime, page))
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
def Getflowdata(res, acountlist):  # 主函数
    ScaleResponse = Get_Data(TrafficScale, res, acountlist)
    QualityResponse = Get_Data(TrafiicQuality, res, acountlist)
    TrafficDatas = DataOptimization(ScaleResponse, QualityResponse)
    return TrafficDatas


# ========================获取询问消息================================
def GetChatData(targeturl, res, acountlist, TimeInfo):
    result = res.get(targeturl % (TimeInfo[0], TimeInfo[1], acountlist[2]))
    return result.text


def Getchatdata(res, acountlist, TimeInfo):
    MerChatResponse = GetChatData(MerChat_api, res, acountlist, TimeInfo)
    MerchatDatas = MeChart_Optimization(MerChatResponse)
    return MerchatDatas


# ======================预约数据 放慢一秒===========================
def Get_appdatalist(data):
    result = []
    addtime = re.search('"addTime":"(.*?)","arriveStatus"',
                        data).group(1).replace('T', ' ')
    userfrom = re.search('"orderSourceVal":"(.*?)","orderTime"', data).group(1)
    usernick = re.search('"customerName":"(.*?)","merchantComment',
                         data).group(1)
    phone = re.search('phoneNo":"(.*?)","productId', data).group(1)
    comment = re.search('comment":"(.*?)","count"', data).group(1)
    status = re.search('"arriveStatusVal":"(.*?)","comment"', data).group(1)
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


def GetAppointresult(res, acountlist):
    page = 1
    num = 2
    Appintdict = {}
    AppointMenttree = Get_appiont_Data(appointment_api, res, page, acountlist)
    MaxPage = int(get_maxpage(AppointMenttree))
    for page in range(1, MaxPage + 1):
        Appointtree = Get_appiont_Data(appointment_api, res, str(page), acountlist)
        AppointData = AppointMent_Optimization(Appointtree)
        for data in AppointData:
            Ddata = Get_appdatalist(data)
            Appintdict[num] = Ddata
            num += 1
    return Appintdict


# ========================线上订单数据================================
def Get_YesterMonth(today):
    return datetime.date(
        today.year - (today.month == 1), today.month - 1 or 12, 1)


# 开始与结束日期
def GetStartandEndDate():
    today = datetime.datetime.today()
    YesterMonth = Get_YesterMonth(today)
    starttime = YesterMonth.strftime("%Y-%m-%d %H:%M:%S")[:10]
    endtime = today.strftime("%Y-%m-%d %H:%M:%S")[:10]
    return starttime, endtime


# 获取HtmlTree
def Get_SaleTree(res, starttime, endtime):
    page = 1
    result = res.get(SaleOnline_html % (str(page), starttime, endtime))
    return result.text


def Get_MaxPage(SaleOnlinetree):
    maxpage = 0
    SaleTree = etree.HTML(SaleOnlinetree)
    pagelist = SaleTree.xpath(
        '//*[@id="deal-consume-form"]/div/div[3]/div[2]/div[1]/div/div/div/a')
    for i in pagelist:
        maxpage += 1
    return maxpage


# 加工返回字典
def GetSaleOnlineresult(res):
    SaleOnlineData = {}
    starttime, endtime = GetStartandEndDate()
    SaleOnlinetree = Get_SaleTree(res, starttime, endtime)
    maxpage = int(Get_MaxPage(SaleOnlinetree))
    for page in range(1, maxpage):
        SaleOnlinetree = res.get(
            SaleOnline_html % (str(page), starttime, endtime)).text
        SaleOnlineData.update(SaleOnline_Optimaization(SaleOnlinetree))
    return SaleOnlineData


# +++==================口碑数据###########################
def Get_CommentTree(res, postData):
    commenttree = res.post(
        Comment_api, data={'postData': json.dumps(postData)}, headers=header)
    return commenttree.text


def GetCommentResult(res, acountlist):
    starttime, endtime = GetStartandEndDate()
    postData = {
        "shopId": acountlist[2],
        "star": "3",
        "projectType": "1",
        "startDate": starttime,
        "endDate": endtime,
        "page": "1",
        "pageSize": "100",
        "reviewState": "0"
    }

    CommentTree = Get_CommentTree(res, postData)
    CommentResult = Commment_Optimaization(CommentTree)

    return CommentResult
