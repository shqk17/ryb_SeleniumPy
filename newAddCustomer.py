from selenium import webdriver
import commonUtils
from selenium.webdriver.support.ui import Select
from time import sleep


def main(customer_num, addtr, username, pawd):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    next_step = True
    driver.get(addtr)
    driver.find_element_by_name('userName').clear()
    driver.find_element_by_name('userName').send_keys(username)
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys(pawd)
    driver.find_element_by_class_name('btn').click()
    ele = driver.find_element_by_class_name('iconWordSpan')
    if len(ele.text) > 0:
        print('登录成功')
    else:
        print("登录失败")
        next_step = False
    if next_step:
        # 打开客户维护页面
        driver.find_element_by_xpath('//*[@class="sidebar-menus open"]/ul/li[3]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//*[@class="sidebar-menus open"]/ul/li[3]/ul/li[1]').click()
        # 点击添加客户按钮
        for i in range(customer_num):
            add_customers(driver)
    input("请输入任意按键退出")
    print("------end------")


# 点击添加客户按钮
def add_customers(driver):
    driver.find_element_by_xpath('//*[@class="add btn btn-success btn-new shiny"]').click()
    driver.find_element_by_id('name').send_keys(commonUtils.GBK2312() + commonUtils.GBK2312())
    driver.find_element_by_name('patriarchName').send_keys(commonUtils.GBK2312() + commonUtils.GBK2312())
    driver.find_element_by_name('contactPhone').send_keys(commonUtils.create_phone())
    channel_source_ele = driver.find_element_by_name('channelSource')
    channel_source_select = Select(channel_source_ele)
    channel_source_select.select_by_index(6)
    affiliation_relation_ele = driver.find_element_by_name('affiliationRelation')
    affiliation_relation_select = Select(affiliation_relation_ele)
    affiliation_relation_select.select_by_index(2)
    driver.find_element_by_xpath('//*[@class="btn btn-orange submitBtn"]').click()
    sleep(2)


if __name__ == "__main__":
    customerNum = 3
    addtr = 'http://localhost:8081/sys_index'
    username = 'fengqiqi'
    pawd = '123456'
    main(customerNum, addtr, username, pawd)
