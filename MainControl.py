# -*- coding: utf-8 -*-
# __auther__ : "johnny leaf"
# __date__: "2018.8.9"
# __project name__ : "dianping_spider"
# __CODE__: Python3

import time

from Edp_excel import report
# from Edp_excel import DataAn
from Spider_edp import dpspider

LoginUrl = 'https://e.dianping.com'

AcounDic = {
    # '八大处亚运村': ['bjykyl', 'ykyl180225', '90030589'],
    # '八大处平安门诊部': ['13883278696', 'bjpa888', '96640607'],
    '煤炭总医院': ['mtzyyzx', 'meitan666', '98380431'],
    # '北京炫美': ['BJxuanmei123456', 'xmzx123456777', '92742255'],
    # '成都健丽': ['cdjianli', 'cdjianli123', '73082729'],
    # '成都美瑞': ['MeiruiTF', 'cdmeirui123', '8352512'],
    # '成都僮颜': ['tongyan88888', 'tongyan61', '98951640'],
    # '德尔美客': ['deermeike', '30826rpo', '97312957'],
    # '瑷珊': ['ieshan23', '37878jmd', '69046169'],
    # '和谐同方': ['HX73357653', '65787488', '4255672'],
    # '时光': ['tjsgzx520', 'tjsgzx2015', '59241747'],
    # '凤凰怡美': ['fenghuangyimei', 'fhymfh1234', '90290461']
}

if __name__ == '__main__':

    for acount in AcounDic:
        res = dpspider.Get_CookeandSession(LoginUrl, AcounDic[acount])
        print('%s 已取得Cookies参数' % acount)
        if res:
            flowresult = dpspider.Getflowdata(res, AcounDic[acount])
            print('%s 已爬取流量数据' % acount)
            chatreuslt = dpspider.Getchatdata(res, AcounDic[acount])
            print('%s 已爬取咨询数据' % acount)
            appointmentresult = dpspider.GetAppointresult(res, AcounDic[acount])
            print('%s 已爬取预约数据' % acount)
            SaleOnlineresult = dpspider.GetSaleOnlineresult(res)
            print('%s 已爬取线上销售数据' % acount)
            CommentResult = dpspider.GetCommentResult(res, AcounDic[acount])
            print('%s 已爬取体验报告' % acount)
            report.Report_main(flowresult, chatreuslt, appointmentresult, SaleOnlineresult, CommentResult, acount)
            print('====全部初始数据导入完毕====')
            print('==========================')
        else:
            time.sleep(1)
    
