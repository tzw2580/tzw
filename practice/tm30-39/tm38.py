# 最大公因数
# 方法一：分别找到两数的因数，再找公因数的最大值
from PIL.Image import blend


def fun1(n):
    lst=[]
    for i in range(1,n+1):
        if n%i == 0:
            lst.append(i)
    return lst

def fun(a,b):
    l1=fun1(a)
    l2=fun1(b)
    # commons=[i for i in l1 if i in l2] #相同元素
    commons=list(set(l1) & set(l2))# 相同元素
    return max(commons)
print(fun(12,18))

# 方法二：辗转相除法
def fun2(a,b):
    while b != 0:
        a,b=b,a%b
    return a
print(fun2(18,64))

# 方法三：较小的数减1，直到能整除这两个数，那么这个数就是最大公因数
def fun3(a,b):
    if a == b:
        return a
    n=min(a,b)
    while a%n != 0 or b%n != 0:
        n-=1
    return n
print(fun3(12,18))
