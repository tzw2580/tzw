# 题目：求矩阵主对角元素之和。
import math
# 将一维列表转换成方阵
lst=list(map(int,input('请输入数据：').strip().split()))
n=int(math.sqrt(len(lst)))
lst1=[lst[i:i+n] for i in range(0,len(lst),n)]
print(lst1)

# 对角线元素求和
s=0
for i in range(len(lst1)):
    for j in range(len(lst1)):
        if i == j:
            s+=lst1[i][j]
print(s)