# n个矩阵相加
lst=[[j+i*3+1 for j in range(3)]for i in range(3)]
n=int(input('请输入n的值：'))
# 方法一
lst_new1=[[(j+i*3+1)*n for j in range(3)]for i in range(3)]
print(lst_new1)
#方法二
lst_new2=[[j*n for j in i] for i in lst]
print(lst_new2)
# 方法三
for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j]=lst[i][j]*n
print(lst)


