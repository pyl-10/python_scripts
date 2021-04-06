#  bag of words 词袋模型

import re

class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        '''
        添加语料(正常来说此处功能为爬虫，搜索器，提供语料)
        '''
        with open(file_path, mode='r') as f:
            text = f.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        '''
        索引器(为语料添加索引)
        '''
        raise Exception(u'未实现语料索引')

    def search(self, query):
        '''
        检索器(用户查询关键词)
        '''
        raise Exception(u'未实现检索功能')


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word in words:
                return True
        return False

    @staticmethod
    def parse_text_to_words(text):
        # 使用正则去除标点符号和换行符
        text = re.sub(r'[^\w]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)


def main(search_engine):
    for file_path in ['out.txt', 'moby_dict.txt', 'myProgramLog.txt']:
        search_engine.add_corpus(file_path)
    while True:
        query = input()
        results = search_engine.search(query)
        print('找到 {} 个结果'.format(len(results)))
        for res in results:
            print(res)

if __name__ == '__main__':
    search_engine = BOWEngine()
    main(search_engine)
