import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''针对AnonymousSurvey类的测试'''

    def setUp(self):
        '''创建一个调查对象和一组答案,供使用的测试方法使用'''
        question = '你第一个学会说的语言是什么? '
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['罗马语', '意大利语', '韩语']


    def test_store_single_response(self):
        '''测试单个答案会被妥善的存储'''
        #question = '你第一个学会说的语言是什么? '
        #my_survey = AnonymousSurvey(question)
        #my_survey.store_response('中文')
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        '''测试三个答案是否会被妥善的存储'''
        #question = '你第一个学会说的语言是什么? '
        #my_survey = AnonymousSurvey(question)
        responses = ['罗马语', '意大利语', '韩语']
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()