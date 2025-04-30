# 题目3：一个整数，它加上 100后是一个完全平方数，再加上268 又是一个完全平方数，请问该数是多少?
# 解方程的思想
def find_num():
    for m in range(1,10000):
        x=m**2-100
        n_squared=x+268
        n=int(math.sqrt(n_squared))
        if n**2 == n_squared:
            return x
    return None
result=find_num()
print(result)

# 以上方法，找到第一个满足条件的x就返回-->-99
# 以下方法，找到所有满足条件的整数-->[-99, 21, 261, 1581]
def findall_num():
    lst=[]
    for m in range(1,10000):
        x=m**2-100
        n_squared=x+268
        n=int(math.sqrt(n_squared))
        if n**2 == n_squared:
            lst.append(x)
    return lst
result=findall_num()
print(result)


