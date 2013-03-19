from sst.actions import *


   
#go to web page
set_base_url('http://www.lequest.nl/website')
go_to('/')
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
sleep(5)








