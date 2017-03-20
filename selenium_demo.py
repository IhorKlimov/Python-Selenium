from array import array
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login():
    email = browser.find_element_by_id('email')
    password = browser.find_element_by_id('pass')
    email.send_keys('your_email')
    password.send_keys('your_password')
    browser.find_element_by_id('u_0_s').submit()

if __name__ == '__main__':
    # browser = webdriver.Firefox(executable_path='./geckodriver')
    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get('https://facebook.com')
    login()
    
    
