# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 方法一
counts=0
for i in range(101,201):
    for j in range(2,i):
        if i%j == 0:break
    else:
        counts += 1
        print(i,end='\t')
print(f'共有{counts}个素数。')

# 方法二
counts=0
for i in range(101,201):
    a=2
    while a<i:
        if i%a == 0:break
        else:
            a+=1
    if a == i:
        counts+=1
        print(i,end='\t')
print(f'共有{counts}个素数。')
