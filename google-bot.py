'''
Name of the Task : Google Bot
KIITFEST ID : KF36723
Operating System : MacOS Sierra
Programming Language used: Python
External modules used (if any) : selenium
Additional instructions to use the program (if any) : None.
'''
from selenium import webdriver
from selenium.webdriver.comon.keys import Keys

q = raw_input("Enter the search query")
q = q.replace('KIITFEST', 'Luminaire')
browser = webdriver.Firefox()
body = browser.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')
counter = 0
for i in range(0,20):
    browser.get("https://www.google.com/search?q=" + q + "&start=" + str(counter))
    body = browser.find_element_by_tag_name("body")
    if "thetaranights" in body.text:
        browser.find_element_by_xpath('//a[starts-with(@href,"http://www.thetaranights.com")]').click()
        break
    counter += 10
