#__auther__ : "johnny leaf"
#__date__: "2018.8.9"
#__project name__ : "dianping_spider"
#__CODE__: Python3.7

import requests
import random
import re
import time
from Edp_excel import report
from Spider_edp import datachange, dpspider
from svc_Edp import svc

target = "http://e.dianping.com"
a = requests.get(target)

if __name__ == '__main__':
    pass