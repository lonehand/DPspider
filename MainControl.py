# -*- coding: utf-8 -*-
# __auther__ : "johnny leaf"
# __date__: "2018.8.9"
# __project name__ : "dianping_spider"
# __CODE__: Python3

from Edp_excel import report
from Spider_edp import dpspider

LoginUrl = 'https://e.dianping.com'

if __name__ == '__main__':

    res = dpspider.Get_CookeandSession(LoginUrl)
    flowresult = dpspider.Getflowdata(res)
    chatreuslt = dpspider.Getchatdata(res)
    report.judge_col(flowresult)
    report.chat_col(chatreuslt)
