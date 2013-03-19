from selenium import selenium
from selenium import webdriver
import unittest
import time

class testUnlocking(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
        
    def test_block(self):
        self.browser.get("http://chaos.ledev.lan:8180")
        self.browser.implicitly_wait(5)
        usernameField = self.browser.find_element_by_xpath('//*[@id="id_username"]')
        passwordField = self.browser.find_element_by_xpath('//*[@id="id_password"]')
        loginButton = self.browser.find_element_by_xpath('//*[@id="signin-form"]/div[2]/form/table/tbody/tr[3]/td/input')
        usernameField.send_keys("robertg")
        passwordField.send_keys("123")
        loginButton.click()
        time.sleep(5)
        self.browser.get("http://chaos.ledev.lan:8180/overview/courses/tmpziehm")
        time.sleep(5)
        
    def test_flash(self):
        self.browser.get("http://gmail.com")
        usernameField = self.browser.find_element_by_xpath('//*[@id="Email"]')
        passwordField = self.browser.find_element_by_xpath('//*[@id="Passwd"]')
        loginButton = self.browser.find_element_by_xpath('//*[@id="signIn"]')
        usernameField.send_keys("testlequest")
        passwordField.send_keys("lequest123")
        loginButton.click()
        time.sleep(5)
        
        
if __name__ == '__main__':
    unittest.main()