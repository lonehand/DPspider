# -*- coding: utf-8 -*-
# CODE - # - OUT
import re
import time

TimeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[10:]


null = 0
false = 0
num = 0

#流量列表
values = []
dates = ''

# 流量字典
DataStructure = {}

# 口碑字典
merchatDict = {}




# ++++++++++++++++ 流量数据+++++++++++++++
def Getlist(data):
    result = data[1:-1].replace('"','').split(",")
    return result

# 流量数据爬取
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
def Get_year(strl):
    result = re.findall('lasContact":"(.*?)","', strl)
    print(result)
    return str(result[:4])

def Get_mouth(strl):
    result = re.search('lasContact":"(.*?)","', strl)
    return result[5:7]

def Get_name(strl):
    result = re.search('clientName":"(.*?)","', strl)
    return result

def Get_firstcontact(strl):
    result = re.search('firstContact":"(.*?)","', strl)
    return result

def Get_lastcontact(strl):
    result = re.search('lastContact":"(.*?)","', strl)
    return result

def Get_Label(strl):
    result = re.search('labelName":"(.*?)","', strl)
    return result

def Get_Shopname(strl):
    result = re.search('shopName":"(.*?)","', strl)
    return result

def Get_branchName(strl):
    result = re.search('branchName":"(.*?)","', strl)
    return result

def MeChart_Optimization(MerChatPage):
    mechartdatas = MerChatPage
    dateslist = re.findall('clientId":(.*?)},{', mechartdatas)
    for i in dateslist:
        dateslist = []
        year = Get_year(i)
        mouth = Get_mouth(i)
        name = Get_name(i)
        firstcontact = Get_firstcontact(i)
        lastcontact = Get_lastcontact(i)
        custmorLable = Get_Label(i)
        shopName = Get_Shopname(i)
        branchName = Get_branchName(i)
        dateslist.append(year)
        dateslist.append(mouth)
        dateslist.append(name)
        dateslist.append(firstcontact)
        dateslist.append(lastcontact)
        dateslist.append(custmorLable)
        dateslist.append(shopName)
        dateslist.append(branchName)
        merchatDict[i] = dateslist
    return merchatDict
