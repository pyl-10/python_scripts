#! python3
# stopwatch.py - 一个简单的秒表计时程序

import time

print('按下"enter"开始计时,按下"click"停止计时,按下"Ctrl-C"退出程序')

input()
print('开始启动')
startTime = time.time()
lastTime = startTime
lapNum = 1  # 记录圈数

try:
    while True:
        input()
        lapTime = round(time.time()-lastTime,2)  # 单圈时间
        totalTime = round(time.time()-startTime,2) # 总和时间
        print('Lap #%s: %s(%s)' %(lapNum,totalTime,lapTime),end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\n完成')