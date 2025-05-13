# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
lst=[]
a,b=1,1
for i in range(1,21):
    a,b=a+b,a
    lst.append('%d/%d'%(a,b))
print(lst)
print(eval('+'.join(lst))) #'+'.join(lst)是str类
