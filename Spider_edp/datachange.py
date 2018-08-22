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
    try:
        result = data[1:-1].replace('"','').split(",")
        return result
    except Exception:
        return '无'

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
    if strl == '':
        return '无记录'
    else:
        year = int(str(re.search('lastContact":"(.*?)","', strl).group(1))[:4])
        return year

def Get_mouth(strl):
    result = re.search('lastContact":"(.*?)","', strl).group(1)
    return int(str(result)[5:7])

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
        print(i)
    for strl in dateslist:
        valueslist = []
        year = Get_year(strl)
        print(year)
        mouth = Get_mouth(strl)
        name = Get_name(strl)
        firstcontact = Get_firstcontact(strl)
        lastcontact = Get_lastcontact(strl)
        custmorLable = Get_Label(strl)
        shopName = Get_Shopname(strl)
        branchName = Get_branchName(strl)
        valueslist.append(year)
        valueslist.append(mouth)
        valueslist.append(name)
        valueslist.append(firstcontact)
        valueslist.append(lastcontact)
        valueslist.append(custmorLable)
        valueslist.append(shopName)
        valueslist.append(branchName)
        merchatDict[year] = valueslist
        
    return merchatDict
