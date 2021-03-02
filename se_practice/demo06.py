from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.support.select import Select

class TestCase(object):
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/forms02.html'
        self.driver.get(file_path)

    def test_select(self):
        se = self.driver.find_element(value='provise')
        select = Select(se)
        # select.select_by_index(2)
        # sleep(2)
        # select.select_by_index(1)
        for option in select.options:
            print(option.text)


if __name__ == '__main__':
    case = TestCase()
    case.test_select()