from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'Username'                #replace the text in the '' with your username
passwordStr = 'Password'                #replace the text in the '' with your password

browser = webdriver.Chrome()
browser.get(('https://ntulearn.ntu.edu.sg/webapps/login/'))

username = browser.find_element_by_id('user_id')
username.send_keys(usernameStr)
password = browser.find_element_by_id('password')
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('entry-login')
signInButton.click()
