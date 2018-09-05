import datetime
import time

today = datetime.datetime.today()
print(datetime.date(today.year - (today.month == 1), today.month - 1 or 12, 1))