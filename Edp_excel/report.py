# -*- coding: utf-8 -*-

import datetime
from openpyxl import load_workbook

sheet_name = ['流量数据', '咨询明细']
filename = ['Report/cicheng.xlsx']

WorkBook = load_workbook(filename[0])
FlowSheet = WorkBook['流量数据']
ChatSheet = WorkBook['咨询明细']


# 获得最大行数
def GetBooklen(sheetname):
    flowbooklen = sheetname.max_row
    return flowbooklen


# 获得昨天
def Get_yesterday():
    today = datetime.datetime.now()
    onedaydelay = datetime.timedelta(days=1)
    yesterday = (today - onedaydelay).strftime(r'%Y-%m-%d')
    return yesterday


# 流量数据管理
def Flowupdate(Data):
    YesterDay = Get_yesterday()
    MaxLen = GetBooklen(FlowSheet)
    LastDay = FlowSheet.cell(MaxLen, 3).value.strftime(r'%Y-%m-%d')
    if YesterDay == LastDay:
        pass
    else:
        for data in Data:
            if data > LastDay:
                FlowSheet.append([
                    '=YEAR(C%s)' % MaxLen,
                    '=MONTH(C%s)' % MaxLen,
                    datetime.datetime.strptime(data, r"%Y-%m-%d"),
                    int(Data[data][0]),
                    int(Data[data][1]),
                    float('%.2f' % float(Data[data][2])),
                    float('%.2f' % float(Data[data][3])),
                ])
        WorkBook.save('Report/cicheng.xlsx')


# 口碑数据管理
def ChatUpdate(Data):
    row = 1
    for data in Data:
        row += 1
        num = 0
        for i in range(1, 8):
            ChatSheet.cell(row, i, value=Data[data][num])
            num += 1
    WorkBook.save('Report/cicheng.xlsx')

# 订单中心