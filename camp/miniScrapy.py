import queue
import requests
from lxml import etree
from queue import Queue
import threading
import json

# 爬虫类
class CrawlThread(threading.Thread):

    def __init__(self) -> None:
        super.__init__()
        self.thread_id = thread_id
        self.queue = queue
        self.headers = {
                'accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, image/webp, */*; q=0.8',
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Mobile Safari/537.36'
            }

    def run(self):
        """
        重写 run 方法
        """
        print(f'启动线程:{self.thread_id}')
        self.scheduler()
        print(f'结束线程:{self.thread_id}')

    def scheduler(self):
        """
        模拟任务调度
        """
        while not self.queue.empty():
            # 队列为空不处理
            page = self.queue.get()
            print(f'下载线程:{self.thread_id}, 下载页面:{page}')
            url = f'https://book/douban.com/top250?start={page*25}'

            try:
                # 下载器


# 页面解析类
class ParserThread(threading.Thread):


if __name__ == '__main__':
    # 定义存放网页的任务队列
    pageQueue = Queue(20)
    for page in range(0, 11):
        pageQueue.put(page)

    # 定义存放解析数据的任务队列
    dataQueue = Queue()

    # 爬虫线程
    crawl_threads = []
    crawl_name_list = ['crawl_1', 'crawl_2', 'crawl_3']
    for thread_id in crawl_name_list:
        thread = CrawlThread(thread_id, pageQueue)
        thread.start()
        crawl_threads.append(thread)

    # 将结果保存到一个json文件中
    with open('book.json', 'a', encoding='utf-8') as pipeline_f:
        # 解析线程
        parse_thread = []
        parser_name_list = ['parse_1', 'parse_2', 'parse_3']
        flag = True
        for thread_id in parser_name_list:
            thread = ParserThread(thread_id, dataQueue, pipeline_f)
            thread.start()

    print('退出主线程')
