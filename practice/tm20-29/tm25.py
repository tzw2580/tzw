# 题目：求1+2!+3!+...+20!的和
# 方法一：
# 自定义函数：求n!
def fun(n):
    if n == 0:
        return 1
    else:
        return n * fun(n-1)
# 求和
s=0
for i in range(1,21):
    s+=fun(i)
print('1+2!+3!+...+20! =',s)

# 方法二：factorial函数
import math
lst=[]
for i in range(1,21):
    lst.append(math.factorial(i))
print('1+2!+3!+...+20! =',sum(lst))

