from openpyxl import load_workbook
import datetime
file_name = 'Report/cicheng.xlsx'
wb = load_workbook(filename=file_name)
table = wb['流量数据']
maxrow = table.max_row
maxcol = table.max_column
lstday = table.cell(maxrow, 3).value


def Get_yesterday():
    today = datetime.datetime.now()
    onedaydelay = datetime.timedelta(days=1)
    yesterday = (today - onedaydelay).strftime(r'%Y-%m-%d')
    return yesterday

for data in Data:
    row = 1
    num = 0
    for i in range(1, 9):
        ws.cell(row+=1,column=1,value=Data[data][num])
        num += 1