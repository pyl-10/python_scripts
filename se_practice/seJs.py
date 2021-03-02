from selenium import webdriver
from time import sleep

class TestCase(object):
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://baidu.com')
    def test1(self):
        self.driver.execute_script('alert("test")')
        sleep(2)
        self.driver.switch_to.alert.accept()
    def test2(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)
    def test3(self):
        js = 'var q = document.getElementById("kw"); q.style.border="2px solid red"'
        self.driver.execute_script(js)
    def test4(self):
        self.driver.find_element(value='kw').send_keys('selenium')
        self.driver.find_element(value='su').click()
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)


if __name__ == "__main__":
    case = TestCase()
    # case.test1()
    # case.test2()
    case.test4()
