from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class TestCase(object):
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://sahitest.com/demo/clicks.htm')

    def test_mouse(self):
        btn = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn).perform() # 双击
        sleep(2)
        btn = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        ActionChains(self.driver).click(btn).perform() # 单击
        sleep(2)
        btn = self.driver.find_element_by_xpath('/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn).perform() # 右键
        sleep(3)

    def test_key(self):
        self.driver.get('http://www.baidu.com')
        kw = self.driver.find_element(value='kw')
        kw.send_keys('selenium')
        kw.send_keys(Keys.CONTROL, 'a')
        sleep(2)
        kw.send_keys(Keys.CONTROL, 'x')
        sleep(2)
        kw.send_keys(Keys.CONTROL, 'v')
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_name('tj_login')).perform()
        sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    case = TestCase()
    # case.test_mouse()
