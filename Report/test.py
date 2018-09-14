# import datetime
# import time
import sys
import datetime
import time
import arrow

endtime = int(time.time()*1000)
print(endtime)
starttime = '2018-01-01'
starttime = arrow.get(starttime).timestamp*1000
print(starttime)