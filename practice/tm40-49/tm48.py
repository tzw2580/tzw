# 使用字典计数
#方法一
# ls1 = list(input())
# ls2 = [ls1.count(i) for i in ls1]
# print(ls1,ls2)
# print(dict(zip(ls1,ls2)))

#方法二
# from collections import Counter
# ls1 = input()
# print(dict(Counter(ls1)))
#方法三：
# ls1 = list(input())
# dict1 = {}
# for i in ls1:
#     if i in dict1:
#         continue
#     dict1[i] = ls1.count(i)
# print(dict1)
# #方法四
# ls1 = list(input())
# dict1 = {}
# for i in ls1:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
# print(dict1)
#方法五
ls1 = list(input())
dict1 = {}
for i in ls1:
    dict1[i] = dict1.get(i,0)+1 #get(i,0)键不存在，默认值为0
print(dict1)