from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def get_element(driver, *loc):
    e = driver.find_element(*loc)
    return e

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://baidu.com')
    sleep(1)
    get_element(driver, By.ID, 'kw').send_keys('selenium')
    get_element(driver, By.ID, 'su').click()