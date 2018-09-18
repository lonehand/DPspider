# -*- coding: utf-8 -*-
# __auther__ : "johnny leaf"
# __date__: "2018.8.9"
# __project name__ : "dianping_spider"
# __CODE__: Python3

import time
import datetime
import sys

from Edp_excel import report
from Edp_excel import DataAn
from Spider_edp import dpspider

LoginUrl = 'https://e.dianping.com'

AcounDic = {
    '测试': [],
    # '八大处亚运村': ['bjykyl', 'ykyl180225', '90030589'],
    # '八大处平安门诊部': ['13883278696', 'bjpa888', '96640607'],
    # '煤炭总医院': ['mtzyyzx', 'meitan000', '98380431'],
    # '北京炫美': ['BJxuanmei123456', 'xmzx123456777', '92742255'],
    # '成都健丽': ['cdjianli', 'cdjs12345', '73082729'],
    # '成都美瑞': ['MeiruiTF', '93963llq', '8352512'],
    # '成都僮颜': ['tongyan88888', 'tongyan61', '98951640'],
    # '德尔美客': ['deermeike', '30826rpo', '97312957'],
    # '瑷珊': ['ieshan23', '37878jmd', '69046169'],
    # '和谐同方': ['HX73357653', '65787488', '4255672'],
    # '时光': ['tjsgzx520', 'tjsgzx2015', '59241747'],
    # '凤凰怡美': ['fenghuangyimei', 'fhymfh1234', '90290461']
}


def GetStartEnddate(label):
    timelist = []
    today = datetime.date.today()
    if label == '半月报':
        day = 1
        timelist.append(str(
            datetime.date(
                today.year - (
                    today.month == 1
                    ), today.month - day or day+11, 1)))
        timelist.append(str(today))
    elif label == '月报':
        starttime = datetime.date(today.year - (today.month == 1), today.month - 2 or 13, 1)
        endtime = datetime.date(today.year - (today.month == 1), today.month - 1 or 12, 31 or 30)
        timelist.append(str(starttime))
        timelist.append(str(endtime))
    else:
        timelist = label.split(' ')
    return timelist


def main(TimeInfo):
    for acount in AcounDic:
        DataAn.main(TimeInfo, acount)
        # res = dpspider.Get_CookeandSession(LoginUrl, AcounDic[acount])
        # print('%s 已取得Cookies参数' % acount)
        # if res:
        #     flowresult = dpspider.Getflowdata(res, AcounDic[acount])
        #     print('%s 已爬取流量数据' % acount)
        #     chatreuslt = dpspider.Getchatdata(res, AcounDic[acount], TimeInfo)
        #     print('%s 已爬取数咨询据' % acount)
        #     appointmentresult = dpspider.GetAppointresult(res, AcounDic[acount])
        #     print('%s 已爬取预约数据' % acount)
        #     SaleOnlineresult = dpspider.GetSaleOnlineresult(res)
        #     print('%s 已爬取线上销售数据' % acount)
        #     CommentResult = dpspider.GetCommentResult(res, AcounDic[acount])
        #     print('%s 已爬取体验报告' % acount)
        #     report.Report_main(flowresult, chatreuslt, appointmentresult, SaleOnlineresult, CommentResult, acount)
        #     print('====%s报表制作完成====' % acount)
        #     print('==========================')
        #     DataAn.main(TimeInfo, acount)
        # else:
        #     time.sleep(1)


def GetUserinput(inputinfo):
    if inputinfo == '半月报':
        timeresult = GetStartEnddate('半月报')
        print('==========%s模式==========' % inputinfo)
    elif inputinfo == '月报':
        timeresult = GetStartEnddate('月报')
        print('==========%s模式==========' % inputinfo)
    else:
        timeresult = GetStartEnddate(inputinfo)
        print('======%s至%s=====' % (timeresult[0], timeresult[1]))
    return timeresult


if __name__ == '__main__':
    userInput = sys.argv[1]
    TimeInfo = GetUserinput(userInput)
    main(TimeInfo)




    
