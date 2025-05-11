# 题目3：一个整数，它加上 100和加上268都是一个完全平方数，请问该数是多少?
import math
# 方法一：解方程的思想
def find_num():
    lst=[]
    for m in range(1,10000):
        x=m**2-100
        n_squared=x+268
        n=int(math.sqrt(n_squared))
        if n**2 == n_squared:
            lst.append(x)
    return lst

result=find_num()
print(result)


# 方法二：
for i in range(10000):
    m=math.sqrt(i+100)
    n=math.sqrt(i+268)
    if m%1 == 0 and n%1 == 0: #判断是不是整数
        print(i)







