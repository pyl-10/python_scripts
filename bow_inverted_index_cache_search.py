# 加上缓存

import re
import pylru

class LRUCache(object):
    def __init__(self, size=32):
        self.cache = pylru.lrucache(size)

    def has(self, key):
        return key in self.cache

    def get(self, key):
        return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value


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


class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.inverted_index = {}

    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)
        for word in words:
            if word in self.inverted_index:
                self.inverted_index[word].append(id)
            self.inverted_index[word] = []

    def search(self, query):
        query_words = list(self.parse_text_to_words(query))
        query_words_index = []
        for query_word in query_words:
            query_words_index.append(0)

        # 如果某个查询单词的倒序索引为空， 就返回
        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []

        result = []
        while True:
            # 获得当前状态下所有倒序索引的index
            current_ids = []

            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]

                # 已经遍历到某个倒序索引的结尾，结束搜索
                if current_index >= len(current_inverted_list):
                    return result

                current_ids.append(current_inverted_list[current_index])

            # 如果 current_ids 的所有元素都一样，就表明这个单词在这个元素对应的文档中都出现了
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue
            # 如果不是，就把最小的元素加一
            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1

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


class BOWInvertedIndexEngineWithCache(BOWInvertedIndexEngine, LRUCache):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        LRUCache.__init__(self)

    def search(self, query):
        if self.has(query):
            print('cache hit')
            return self.get(query)

        result = super(BOWInvertedIndexEngineWithCache, self).search(query)
        self.set(query, result)

        return result


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
    search_engine = BOWInvertedIndexEngineWithCache()
    main(search_engine)
