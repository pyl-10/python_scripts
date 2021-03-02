from  selenium import webdriver
import os
from time import sleep

class TsetCase(object):
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/forms.html'
        # print(file_path)
        self.driver.get(file_path)
    def test_login(self):
        self.driver.find_element(value='username').send_keys('admin')
        self.driver.find_element(value='pwd').send_keys('123')
        sleep(2)
        self.driver.find_element(value='submit').click()
        self.driver.switch_to.alert.accept()    # 消除alert

if __name__ == '__main__':
    case = TsetCase()
    case.test_login()
