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
        list = []
        for i in range(customer_num):
            p = {'A': add_customers(driver),'B':add_customers(driver)}
            list.append(p)

        # 转会员了
    for i in range(len(list)):
        driver.find_element_by_xpath('//*[@targetname="' + list[i].get("A") + '"]').click()
        sleep(0.2)
        driver.find_element_by_name('contractNumber').send_keys(commonUtils.get_clice())
        pacakage_ele = driver.find_element_by_name('dearSonPackageId')
        pacakage_eleselect = Select(pacakage_ele)
        pacakage_eleselect.select_by_index(2)

        applyStatus_qz_ele = driver.find_element_by_name('applyStatus_qz')
        applyStatus_qz_eleselect = Select(applyStatus_qz_ele)
        applyStatus_qz_eleselect.select_by_index(1)

        moneyJs = "return $('#dearSonPackageSumPrice').val();"
        money = driver.execute_script(moneyJs)

        driver.find_element_by_name('dearSonPackageDiscountSumPrice').send_keys(money)
        js = "$('input[id=d1312_qz]').removeAttr('readonly')"
        js2 = "$('input[id=d1312_qz]').removeAttr('onfocus')"
        driver.execute_script(js)
        driver.execute_script(js2)
        driver.find_element_by_name('paymentTime').send_keys('2018-12-14')

        js = "$('input[id=dearSonUserUeffectiveStartTime]').removeAttr('readonly')"
        js2 = "$('input[id=dearSonUserUeffectiveStartTime]').removeAttr('onfocus')"
        driver.execute_script(js)
        driver.execute_script(js2)
        driver.find_element_by_name('userUeffectiveStartTime').send_keys('2018-12-14')

        js = "$('input[id=dearSonUserUeffectiveEndTime]').removeAttr('readonly')"
        js2 = "$('input[id=dearSonUserUeffectiveEndTime]').removeAttr('onfocus')"
        driver.execute_script(js)
        driver.execute_script(js2)
        driver.find_element_by_name('userUeffectiveEndTime').send_keys('2018-12-14')

        js = "$('input[id=dearSonUserSignTime]').removeAttr('readonly')"
        js2 = "$('input[id=dearSonUserSignTime]').removeAttr('onfocus')"
        driver.execute_script(js)
        driver.execute_script(js2)
        driver.find_element_by_name('signTime').send_keys('2018-12-14')

        dearSonStaffId_ele = driver.find_element_by_name('dearSonStaffId')
        dearSonStaffId_select = Select(dearSonStaffId_ele)
        dearSonStaffId_select.select_by_index(1)

        post_ele = driver.find_element_by_name('post')
        post_select = Select(post_ele)
        post_select.select_by_index(1)

        staffName_ele = driver.find_element_by_name('staffNames')
        staffName_select = Select(staffName_ele)
        staffName_select.select_by_index(1)

        driver.find_element_by_name('proportion').send_keys('1')
        sleep(0.1)
        driver.find_element_by_xpath('//*[@class="btn btn-new toPackageEditFormSubmitBtn"]').click()
    input("请输入任意按键退出")
    print("------end------")


# 点击添加客户按钮
def add_customers(driver):
    driver.find_element_by_xpath('//*[@class="add btn btn-success btn-new shiny"]').click()
    username = commonUtils.getChineseName()
    driver.find_element_by_id('name').send_keys(username)
    driver.find_element_by_name('patriarchName').send_keys(commonUtils.getChineseName())
    driver.find_element_by_name('contactPhone').send_keys(commonUtils.create_phone())
    channel_source_ele = driver.find_element_by_name('channelSource')
    channel_source_select = Select(channel_source_ele)
    channel_source_select.select_by_index(6)
    affiliation_relation_ele = driver.find_element_by_name('affiliationRelation')
    affiliation_relation_select = Select(affiliation_relation_ele)
    affiliation_relation_select.select_by_index(2)
    driver.find_element_by_xpath('//*[@class="btn btn-orange submitBtn"]').click()
    sleep(2)
    return username


if __name__ == "__main__":
    # 生产几组绑定课时包数据
    bindGroup = 1
    addtr = 'http://localhost:8081/sys_index'
    # username = 'fengqiqi'
    # pawd = '123456'
    username = 'shuhaoyz'
    pawd = 'qzy123456'
    main(bindGroup, addtr, username, pawd)
