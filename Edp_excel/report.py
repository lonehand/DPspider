# -*- coding: utf-8 -*-

import datetime
import os

import xlrd
import xlwt
from xlutils.copy import copy

today = datetime.date.today()
year = int(str(today)[:4])
mouth = int(str(today)[5:7])
workbook_read = xlrd.open_workbook('./Report/cicheng.xls', formatting_info=True)
sheet_read = workbook_read.sheet_by_name("流量数据")
excel_copy = copy(workbook_read)
sheet_copy = excel_copy.get_sheet('流量数据')
booklen = sheet_read.nrows

# 样式
# def datastyle(name, height,color, bold=False):
#     style = xlwt.XFStyle()  # 初始化样式
#     font = xlwt.Font()
#     font.name = name
#     font.colour_index = color
#     font.height = height
#     style.font = font
#     alignment = xlwt.Alignment()
#     alignment.horz = color
#     style.alignment = alignment
#     return style

def Get_yesterday(today):
    onedaydelay = datetime.timedelta(days=1)
    yesterday = today - onedaydelay
    return yesterday

def Get_lastdate(sheet_read):
    lastdates = int(sheet_read.cell_value(booklen-1, 2))
    lastdate = xlrd.xldate.xldate_as_datetime(lastdates, 0)
    return lastdate

def judge_col(Data):
    listlen = booklen
    lastdate = str(Get_lastdate(sheet_read))
    for i in Data:
        Datalist = []
        if i > lastdate:
            num = 0
            Datalist.append(year)
            Datalist.append(mouth)
            Datalist.append(datetime.datetime.strptime(i, "%Y-%m-%d"))
            Datalist.append(int(Data[i][0]))
            Datalist.append(int(Data[i][1]))
            Datalist.append(float('%.2f' %float(Data[i][2])))
            Datalist.append(float('%.2f' %float(Data[i][3])))
            for title in range(0, 7):
                sheet_copy.write(listlen, title, Datalist[num])
                num += 1
            listlen += 1
            print(i,"已更新")
        else:
            pass
        
    os.remove(r'./Report/cicheng.xls')
    excel_copy.save(r'./Report/cicheng.xls')

