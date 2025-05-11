'''
题目：斐波那契数列。斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
'''
# 方法一
lst=[0,1]
dep=20 #数列长度
for i in range(dep-2):
    x=lst[i]+lst[i+1]
    lst.append(x)
print(lst)
# 方法二
lst1=[0,1]
x,y=0,1
for i in range(dep-2):
    x,y=y,x+y
    lst1.append(y)
print(lst1)


