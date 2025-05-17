# 题目：给定一个字符串，请你判断其中每个字符是否全都不同。
# 方法一：
def fun1(s:str):
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return False
    return True
print(fun1('Hello world'))

# 方法二：
def fun2(s:str):
    for i in s:
        n=s.count(i)
        if n >= 1:
            return False
    return True
print(fun2('Hello world'))