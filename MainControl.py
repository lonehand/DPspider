# -*- coding: utf-8 -*-
# __auther__ : "johnny leaf"
# __date__: "2018.8.9"
# __project name__ : "dianping_spider"
# __CODE__: Python3

from Spider_edp import dpspider

LoginUrl = 'https://e.dianping.com'

if __name__ == '__main__':

    res = dpspider.Get_CookeandSession(LoginUrl)
    flowresult = dpspider.Getflowdata(res)
    chatreuslt = dpspider.Getchatdata(res)
    appointmentresult = dpspider.GetAppointresult(res)
    SaleOnlineresult = dpspider.GetSaleOnlineresult(res)
    # report.Flowupdate(flowresult)
    # report.ChatUpdate(chatreuslt)
    # report.AppointUpdate(appointmentresult)
    # report.SaleOnlineUpdate(SaleOnlineresult)
