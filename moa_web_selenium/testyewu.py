from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from time import sleep
from selenium.webdriver import support
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait;
driver = webdriver.Chrome()
driver.implicitly_wait(5)
base_url = "https://200.200.169.212/"
driver.get(base_url)
driver.find_element_by_id("id-username").clear()
driver.find_element_by_id("id-username").send_keys("12200000000")
driver.find_element_by_id("id-pwd").clear()
driver.find_element_by_id("id-pwd").send_keys("12345")
driver.find_element_by_id("id-sn").clear()
driver.find_element_by_id("id-sn").send_keys("2")
driver.find_element_by_id("id-btn").click()
#引进问题
# WebDriverWait(driver, 10).until(driver.find_element_by_id('kw')) # 错误

driver.find_element_by_xpath("//li[@namemark='Task']").click()
sleep(2)
driver.find_element_by_xpath("//span[contains(text(),'发布的任务')]").click()
sleep(4)

#不能直接使用id定位，每个人登陆以后的id会不断变化，要使用唯一名称
# driver.find_element_by_link_text("创建任务").click()
# driver.find_element_by_id("ext-comp-1110").click()

# print(driver.find_elements_by_xpath("//table/tbody/tr[2]/[contains(text(),'创建任务')]").count())
driver.find_element_by_xpath("//button[contains(text(),'创建任务')]").click()
sleep(4)
driver.find_element_by_name("content").send_keys("dddddddautotest")
# driver.find_element_by_name("deadline").clear()
driver.find_element_by_name("deadline").click()
sleep(1)
driver.find_element_by_xpath("//td[@title=\"今天\"]").click()
# driver.find_element_by_xpath("//*[contains(text(),'24')]").click()
# sleep(1)
# #模拟双击
at = ActionChains(driver);

at.double_click(driver.find_element_by_xpath("//span[contains(text(),'24')]"))
at.drag_and_drop()
# sleep(3)
# driver.find_element_by_name("members").click()
#
# # driver.find_element_by_id("ext-comp-1129").clear()
# sleep(2)
# driver.find_element_by_xpath("//input[@placeholder='搜索成员']").click()
print(driver.find_element_by_xpath("//div[@class=\"x-tool x-tool-close\"]"))
driver.find_element_by_xpath("//div[@class=\"x-tool x-tool-close\"]").click()
# driver.find_element_by_xpath("//div[@class=\"x-tool x-tool-close\"]")[1].click()


#为什么当有两个弹窗页面的时候，关闭不了，不能够挨个关闭