import datetime
import time


def Get_YesterMonth(today):
    return datetime.date(today.year - (today.month == 1), today.month - 1 or 12, 1)

today = datetime.datetime.today()
YesterMonth = Get_YesterMonth(today)
starttime = YesterMonth.strftime("%Y-%m-%d %H:%M:%S")
endtime = today.strftime("%Y-%m-%d %H:%M:%S")

timeArray1 = time.strptime(endtime, "%Y-%m-%d %H:%M:%S")[:10]
timeArray2 = time.strptime(starttime, "%Y-%m-%d %H:%M:%S")[:10]
endtime = time.mktime(timeArray1)
starttime = time.mktime(timeArray2)

print(int(endtime*1000))
print(int(starttime*1000))