from aip import  AipOcr

'''
图片输入
图片预处理
文字检测
文字识别
输出
'''

# 你的APPID AK SK
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content('demo.jpg')
# 调用通用文字识别， 图片参数为本地图片
result = client.basicGeneral(image)
info = []
for i in result['words_result']:
    info.append(i['words'])
print(info)
