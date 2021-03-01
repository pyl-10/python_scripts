import shutil,os,re

datePattern = re.compile(r'''^(.*?) # 匹配日期出现之前的任何文本
        ((0|1)?\d) -                # 月份
        ((0|1|2|3)?\d) -            # 日期
        ((19|20)\d\d)               # 年
        (.*?)$                      # 匹配日期之后的任何文本
        ''',re.VERBOSE)