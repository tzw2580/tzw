# 题目：格式化输出当前时间。
# 法一
import time
print('当前时间：',time.strftime('%Y-%m-%d,%H:%M:%S',time.localtime()))

# 法二
from datetime import datetime
nowdt=datetime.now()
nowdt_str=nowdt.strftime('%Y-%m-%d,%H:%M:%S')
print('当前时间：',nowdt_str)