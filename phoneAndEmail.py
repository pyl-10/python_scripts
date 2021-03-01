import pyperclip, re

# 电话号码正则
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                     # 匹配"可选的"区号 匹配结果:123 or (123) 可有可无De区号
    (\s|-|\.)?                             # 匹配 空格 or - or .句号  可有可无De分隔符
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

# 邮箱地址正则
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                      # 匹配用户名
    @
    [a-zA-Z0-9.-]
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# 在 剪切板文本中查找所有符合要求的匹配字符串
text = str(pyperclip.paste())
print(text)
matches = []
for groups in phoneRegex.findall(text):
    print(groups)
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for emailGroup in emailRegex.findall(text):
    print(emailGroup)
    matches.append(emailGroup[0])

# 将匹配结果连接成一个字符串 ,复制到剪贴板
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('结果为:')
    print('\n'.join(matches))
else:
    print('没有符合的匹配结果')