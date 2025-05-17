# 在一个字符串中找到第一个只出现一次的字符,并返回它的位置,如果没有则返回 -1(需要区分大小写).(从0开始计数)
# 方法一：字典统计
s='pythonproject'
a=-1
# 统计每个字符出现的次数
mp={}
for i in s:
    if i not in mp:
        mp[i]=1
    else:
        mp[i]+=1
print(mp)

# 找到第一个只出现一次的字符，并返回它的位置
for i in range(len(s)):
    if mp.get(s[i]) == 1:
        a=i #更新返回的位置
        break
print(a)
# 找到第一个只出现一次的字符，并返回它的位置
for index,char in enumerate(s):
    if mp[char] == 1:
        print(index)
        break

# 方法二：常规方法
def fun(s:str):
    for index,char in enumerate(s):
        n=s.count(char)
        if n == 1:
            return index
    return -1
print(fun('aabcc'))



