# -*- coding: utf-8 -*-
# CODE - # - OUT
import re
import time

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
    salelist = []
    saledic = {}
    SaleData = re.search('"orderList":\[(.*?)\]}]},"code":', SaleOnlinetree).group(1)[1:-1].replace('},{', '?').split('?')
    for data in SaleData:
        saletime = re.search('"verifyTime":"(.*?),"mobile"', data).group(1)
        productname = re.search('"productItemName":"(.*?)","shopId"', data).group(1)
        userphoen = re.search('"mobile":"(.*?)","availableCouponCount', data).group(1)
        shopname = re.search('"shopName":"(.*?)","addTime', data).group(1)




