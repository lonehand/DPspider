# -*- coding: utf-8 -*-
# CODE - # - OUT
import re
import time
from lxml import etree
from lxml.html import fromstring, tostring

TimeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[10:]

null = 0
false = 0
num = 0

# 流量数据结构
values = []
dates = ''
DataStructure = {}

# 口碑数据结构
merchatDict = {}
chatvalues = []


# ++++++++++++++++ 流量数据+++++++++++++++
def Getlist(data):
    try:
        result = data[1:-1].replace('"', '').split(",")
        return result
    except Exception:
        return '无'


# ++++++++++++++++ 流量数据 ++++++++++++++++++
def DataOptimization(ScaleResponse, QualityResponse):
    try:
        global num
        DatesData = re.search('dates":(.*?),"detail', ScaleResponse).group(1)
        Scaleresult = re.findall('false,"value":(.*?)},', ScaleResponse)
        Qualityresult = re.findall('false,"value":(.*?)},', QualityResponse)
        PvData = Scaleresult[0]
        DauData = Scaleresult[3]
        stayData = Qualityresult[0]
        lostData = Qualityresult[3]
        DatesData = Getlist(DatesData)
        PvData = Getlist(PvData)
        DauData = Getlist(DauData)
        stayData = Getlist(stayData)
        lostData = Getlist(lostData)
        for dateinfo in DatesData:
            values = []
            values.append(PvData[num])
            values.append(DauData[num])
            values.append(stayData[num])
            values.append(lostData[num])
            DataStructure[dateinfo] = values
            num += 1
    except Exception as e:
        print(e)
    return DataStructure


# ++++++++++++++++++++++++++口碑数据+++++++++++++++++++++++
def Get_MeChartData(chatDataList):
    global chatvalues
    chatvalues = []
    for info in chatDataList:
        chatvalues = []
        try:
            timedata = re.search('lastContact":"(.*?)","us', info).group(1)
            year = int(timedata[:4])
            mounth = int(timedata[5:7])
            nick = re.search('clientName":"(.*?)","ph', info).group(1)
            firsttalk = re.search('firstContact":"(.*?)","la', info).group(1)
            label = re.search('"labelName":"(.*?)"}', info).group(1)
            shop = re.search('shopName":"(.*?)","bran', info).group(1)
            chatvalues.append(year)
            chatvalues.append(mounth)
            chatvalues.append(nick)
            chatvalues.append(firsttalk)
            chatvalues.append(timedata)
            chatvalues.append(label)
            chatvalues.append(shop)
            merchatDict[nick] = chatvalues
        except Exception as error:
            error
            continue
    return merchatDict


def MeChart_Optimization(MerChatPage):
    merchatDict = {}
    try:
        chatInfo = re.search('"records":(.*?)}]},"errorMsg"',
                             MerChatPage).group(1)
        chatData = chatInfo[1:-1].replace('},', '&')
        chatDataList = chatData.split('&')
        try:
            merchatDict = Get_MeChartData(chatDataList)
        except Exception as e:
            return e
    except Exception as e:
        return e
    return merchatDict


def AppointMent_Optimization(AppointMenttree):
    Tdata = re.search(
        '"records":\[(.*?)\],"sortAsc":', AppointMenttree, re.S
        ).group(1).replace(' ', '').replace('},{', '?')[1:-1]
    result = Tdata.split('?')
    return result


def SaleOnline_Optimaization(SaleOnlinetree):
    saledict = {}
    htmltree = etree.HTML(SaleOnlinetree)
    data = htmltree.xpath('//*[@id="consume-detail-list"]/thead')[0]
    original_html = etree.tostring(data, encoding='utf-8', pretty_print=True, method='html')
    htmlstr = str(original_html, encoding="utf-8").replace(' ', '').replace('\n', '').replace('-', '0')
    htmllist = re.findall('<tr>(.*?)</tr>', htmlstr)
    for data in htmllist[1:]:
        resultlist = []
        htmldata = re.findall('<td>(.*?)</td>', data)
        if htmldata[5] == '0':
            pass
        else:
            htmldata[5] = re.search('<div>团购立减:(.*?)</div>', htmldata[5]).group(1)
        resultlist.append(int(htmldata[2][:4]))
        resultlist.append(int(htmldata[2][5:7]))
        resultlist.append(float(htmldata[4])-float(htmldata[5]))
        resultlist.append(int(htmldata[0]))
        resultlist.append(htmldata[1])
        resultlist.append(htmldata[2][:4]+'/'+htmldata[2][5:7]+'/'+htmldata[2][8:10])
        resultlist.append(htmldata[2][10:])
        if htmldata[3][0] != '<':
            resultlist.append(htmldata[3])
        else:
            resultlist.append(re.search('">(.*?)</a>', htmldata[3]).group(1))
        resultlist.append(float(htmldata[4]))
        resultlist.append(float(htmldata[5]))
        resultlist.append(float(htmldata[6]))
        resultlist.append(htmldata[8])
        resultlist.append(htmldata[9])
        saledict[htmldata[0]] = resultlist
    return saledict
        
        



    





