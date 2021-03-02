from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.support.select import Select

class TestCase(object):
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/forms03.html'
        self.driver.get(file_path)
    def test_alert(self):
        self.driver.find_element(value='alert').click()
        # 切换到alert
        alert = self.driver.switch_to_alert()
        print(alert.text)
        sleep(3)
        alert.accept()
    def test_confirm(self):
        self.driver.find_element(value='confirm').click()
        confirm = self.driver.switch_to_alert()
        print(confirm)
        sleep(3)
        confirm.dismiss()
    def test_prompt(self):
        self.driver.find_element(value='prompt').click()
        prompt = self.driver.switch_to_alert()
        print(prompt.text)
        prompt.accept()
        sleep(5)

if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()
