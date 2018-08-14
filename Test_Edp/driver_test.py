import time

import requests
import selenium.webdriver.support.ui as ui
from selenium import webdriver, webdriver
from selenium.webdriver import ActionChains



#=========================爬虫模块测试==============================#

# 目标
target = r"https://epassport.meituan.com/account/unitivelogin?bg_source=2&service=dpmerchantlogin&feconfig=dpmerchantlogin&leftBottomLink=https://e.dianping.com/shopaccount%2fphoneRegisterAccount&continue=https%3A%2F%2Fe.dianping.com%2Fshopaccount%2Flogin%2Fsetedper%3FtargetUrl%3Dhttps%253A%252F%252Fe.dianping.com%252Fshopportal%252Fpc%252Fnewindex"

# 账号与密码
Account = ["meiruiTF", "cdjianli","bjykyl,"]
Password = ["cdmeirui123","cdjianli123","ykyl180225,"]

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("disable-infobars")
ChromeBrowser = webdriver.Chrome(options=ChromeOptions)
RowAction = ActionChains(ChromeBrowser)

ChromeBrowser.get(target)
time.sleep(0.3)
ChromeBrowser.find_element_by_xpath('//*[@id="login"]').send_keys(Account[0])
ChromeBrowser.find_element_by_xpath('//*[@id="password"]').send_keys(Password[0])
ChromeBrowser.find_element_by_xpath('//*[@id="login-form"]/button').submit()
time.sleep(0.5)
if ChromeBrowser.find_element_by_xpath('//*[@id="yodaBox"]'):
    ScrollBar = ChromeBrowser.find_element_by_xpath('//*[@id="yodaBox"]')
    RowAction.click_and_hold(ScrollBar)
    for i in range(0,198):
        if i != 197:
            RowAction.move_by_offset(i,0)
        else:
            RowAction.release()
    RowAction.perform()

#===================================================================#




