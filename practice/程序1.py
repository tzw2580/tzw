# 题目1：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数?都是多少?
import math

count=0
print('数字','个数')
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                print(i,j,k,sep='',end='\t')
                count+=1 # 记录个数
                print(count)