# 题目：求阶乘5！
# 方法一：递归
def fun(n):
    if not isinstance(n,int): #判断n是否为整型
        raise TypeError
    if n < 0:
        raise Exception
    if n == 0:
        return 1
    else:
        return n * fun(n-1)
print(fun(5))

# 方法二
s=1
for i in range(1,6):
    s*=i
print(s)