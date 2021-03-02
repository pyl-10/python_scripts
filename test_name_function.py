import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''测试name_function.py'''

    def test_first_last_name(self):
        '''测试是否能够正确处理像one piece这样的姓名'''
        formatted_name = get_formatted_name('one','piece')
        self.assertEqual(formatted_name,'One Piece')

    def test_first_middle_last_name(self):
        '''测试能否正确处理像one two three这样的姓名'''
        formatted_name = get_formatted_name('one','two','three')
        self.assertEqual(formatted_name,'One Three Two')

unittest.main()