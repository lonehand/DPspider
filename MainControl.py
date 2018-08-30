# -*- coding: utf-8 -*-
#__auther__ : "johnny leaf"
#__date__: "2018.8.9"
# __project name__ : "dianping_spider"
#__CODE__: Python3

import re
import time
from Edp_excel import report
from Spider_edp import dpspider
from svc_Edp import svc

if __name__ == '__main__':
    result = dpspider.spidermain()
    report.judge_col(result)
