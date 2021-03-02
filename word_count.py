def count_words(filename):
    """计算一个文件大致包含多少单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        # msg = '没找到文件'
        # print(msg)
    else:
        words = contents.split()
        new_words = len(words)
        print(new_words)

        count_word = 0

        for word in words:
            count_word += word.lower().count('you')

        print(count_word)

filenames = ['alice.txt','little_women.txt','moby_dict.txt','siddhartha.txt']
for filename in filenames:
    count_words(filename)