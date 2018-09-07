# import datetime
# import re

# test = '''
# "mainOrderId":37181652,"uniOrderId":"153214554474475290609284","orderStatus":4,"couponValue":"45742114452","productId":3834360,"productItemId":14196495,"cooperationBizType":850,"productItemName":"润百颜1ML·首次体验价","shopId":73082729
# ,"shopName":"成都健丽医疗美容","addTime":1532145544000,"verifyTime":1535775368000,"mobile":"186****4959","availableCouponCount":0,"refundCouponCount":0,"price":466.00,"quantity":1,"preAmount":192.00,"remainAmount":0.00,"payTypeList":["
# 点评扫码","微信扫码","支付宝扫码","现金支付","刷卡支付","其他"],"discountDetailDTOList":[{"discountType":17,"discountAmount":234.00,"discountName":"商家立减","refundable":false
# 1535775368000
# '''

# a = re.search(r'verifyTime":(.*?),"mobile', test).group(1)

# html = 'https://e.dianping.com/receiptreport/tuangouConsumeDetail?page=%s&selectedBeginDate=%s%%2000:00:00&selectedEndDate=%s%%2000:00:00'
# print(html % ('1','2','3'))
from openpyxl import load_workbook
filename = ['meirui.xlsx']
WorkBook = load_workbook(filename[0])
FlowSheet = WorkBook['流量']
print(FlowSheet.max_row)

