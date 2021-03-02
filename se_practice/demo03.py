from selenium import webdriver
from time import sleep

class TestCase(object):
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://bing.com')
        self.driver.maximize_window()

    def test_prop(self):
        print(self.driver.name) # 浏览器名称
        print(self.driver.current_url) # 当前url
        print(self.driver.title)
        print(self.driver.window_handles)
        print(self.driver.page_source)
        self.driver.quit()

    def test_method(self):
        self.driver.find_element(value='sb_form_q').send_keys('selenium')
        self.driver.find_element(value='sb_form_go').click()
        sleep(2)
        self.driver.back()
        sleep(2)
        self.driver.refresh()
        sleep(2)
        self.driver.forward()
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    test = TestCase()
    #test.test_prop()
    test.test_method()
