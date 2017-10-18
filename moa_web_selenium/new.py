# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://200.200.169.212/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("id-username").clear()
        driver.find_element_by_id("id-username").send_keys("12200000001")
        driver.find_element_by_id("id-pwd").clear()
        driver.find_element_by_id("id-pwd").send_keys("12345")
        driver.find_element_by_id("id-sn").clear()
        driver.find_element_by_id("id-sn").send_keys("2")
        driver.find_element_by_id("id-btn").click()
        driver.find_element_by_xpath("//div[@id='ext-gen20']/ul/li[6]").click()
        driver.find_element_by_xpath("//ul[@id='ext-gen77']/li[2]/span[2]").click()
        driver.find_element_by_id("ext-gen87").click()
        driver.find_element_by_id("ext-comp-1116").clear()
        driver.find_element_by_id("ext-comp-1116").send_keys("232132132")
        driver.find_element_by_id("ext-comp-1117").click()
        driver.find_element_by_xpath(
            "//table[@id='ext-gen153']/tbody/tr[2]/td/table/tbody/tr[3]/td[5]/a/em/span").click()
        driver.find_element_by_id("ext-comp-1119").click()
        driver.find_element_by_id("ext-comp-1129").clear()
        driver.find_element_by_id("ext-comp-1129").send_keys("ceshiyi")
        driver.find_element_by_css_selector("dd..over").click()
        driver.find_element_by_id("ext-comp-1136").click()
        driver.find_element_by_id("ext-gen132").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
