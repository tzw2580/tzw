# 猜数字游戏
import random
x=random.randint(0,100)
counts=0 #统计猜的次数
while counts <= 7:
    y=int(input('请输入猜的数字：'))
    if y > x:
        print('大了！')
        counts+=1
    elif y < x:
        print('小了！')
        counts+=1
    else:
        print('猜对了！')
        break
