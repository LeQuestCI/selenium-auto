import unittest
import selenium
from selenium import webdriver
from sst.actions import *

class NuNlTestHomePage(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
        
    def test_Title(self):
        set_base_url('http://www.lequest.nl/website')
        go_to('/')
        sleep(3)
        contactLink = get_element_by_xpath('//*[@id="menu-item-44"]/a')
        click_element(contactLink, True)
        assert_title_contains('Contact')
        
        #insert name into name field    
        nameField = get_element_by_xpath('//*[@id="wpcf7-f539-p42-o1"]/form/p[1]/span/input')
        assert_textfield(nameField)
        write_textfield(nameField, 'Django Tarantino', False, True)
        sleep(2)
        
        #insert email address into email field
        emailField = get_element_by_xpath('//*[@id="wpcf7-f539-p42-o1"]/form/p[2]/span/input')
        assert_textfield(emailField)
        write_textfield(emailField, 'graauw@lequest.nl', False, True)
        sleep(2)
        
        # add text to message field in contact form
        messageField = get_element_by_xpath('//*[@id="wpcf7-f539-p42-o1"]/form/p[3]/span/textarea')
        assert_textfield(messageField)
        write_textfield(messageField, 'Dit is een automatisch gegenereerd bericht. U kunt dit bericht gerust negeren. Met vriendelijke groet, Selenium Testing Script', False, True)
        
        
        
    def test_contact_page_loaded(self):
        base_url = 'http://www.nu.nl'
        self.browser.get(base_url)
        sportLink = self.browser.find_element_by_xpath('//*[@id="extensionnav"]/ul/li[3]/a')
        sportLink.click()
        self.browser.implicitly_wait(5)
        self.assertIn('Contact', self.browser.title)
        
    def test_contact_page_contains_contact_form(self):
        set_base_url('http://www.lequest.nl/website')
        go_to('http://www.lequest.nl/website')
        go_to('/contact')
        nameField = get_element_by_xpath('//*[@id="wpcf7-f539-p42-o1"]/form/p[1]/span/input')
        assert_textfield(nameField)
        write_textfield(nameField, 'Django Tarantino', False, True)
    

        
if __name__ == '__main__':
    unittest.main()