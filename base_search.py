class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as f:
            text = f.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('process_corpus not')

    def search(self, query):
        raise Exception('search not')

class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results

def main(search_engine):
    for file_path in ['out.txt', 'moby_dict.txt', 'myProgramLog.txt']:
        search_engine.add_corpus(file_path)
    while True:
        query = input()
        res = search_engine.search(query)
        print('找到 {} 个结果:'.format(len(res)))
        for result in res:
            print(result)

if __name__ == '__main__':
    search_engine = SimpleEngine()
    main(search_engine)

