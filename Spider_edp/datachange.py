# -*- coding: utf-8 -*-
# CODE - # - OUT
import re

null = 0
false = 0

Dates = {
    '日期': '0',
    'PV': '0',
    'DAU': '0'
}

def Getlist(data):
    result = data[1:-1].replace('"','').split()
    return result

def DataOptimization(Response):
    DatesData = re.search('dates":(.*?),"detail', Response).group(1)
    PvData = re.search('false,"value":(.*?)},', Response).group(1)
    Dates['日期'] = Getlist(DatesData)
    Dates['PV'] = Getlist(PvData)
    print(Dates['日期'])
    print(Dates['PV'])
    return 1
