from selenium import webdriver
import random
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
nextStep = True
driver.get("http://localhost:8081/sys_index")
driver.find_element_by_name('userName').clear()
driver.find_element_by_name('userName').send_keys('fengqiqi')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_class_name('btn').click()
ele = driver.find_element_by_class_name('iconWordSpan')
if len(ele.text) > 0:
    print('登录成功')
else:
    print("登录失败")
    nextStep = False
# 打开客户维护页面
driver.find_element_by_xpath('//*[@class="sidebar-menus open"]/ul/li[3]').click()
driver.find_element_by_xpath('//*[@class="sidebar-menus open"]/ul/li[3]/ul/li[1]').click()
# 点击添加客户按钮
driver.find_element_by_xpath('//*[@class="add btn btn-success btn-new shiny"]').click()


def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = f'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str


s = GBK2312()
driver.find_element_by_id('name').send_keys(s + s)
driver.find_element_by_name('patriarchName').send_keys(s + s)
driver.find_element_by_name('contactPhone').send_keys('18628185775')
channelSourceEle = driver.find_element_by_name('channelSource')
channelSourceSelect = Select(channelSourceEle)
channelSourceSelect.select_by_index(6)
affiliationRelationEle = driver.find_element_by_name('affiliationRelation')
affiliationRelationSelect = Select(affiliationRelationEle)
affiliationRelationSelect.select_by_index(2)
driver.find_element_by_xpath('//*[@class="btn btn-orange submitBtn"]').click()
print("------end------")
