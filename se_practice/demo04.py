from selenium import webdriver
from time import sleep

from selenium.webdriver.remote.webelement import WebElement

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')

    def test_webelement_prop(self):
        e = self.driver.find_element(value='t1')
        e1 = WebElement
        print(type(e))
        print(e.id)
        print(e.tag_name)
        print(e.size)
        print(e.rect)
        print(e.text)

if __name__ == '__main__':
    case = TestCase()
    case.test_webelement_prop()