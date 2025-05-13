# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
n = int(input('请输入一个正整数：'))
k=2
lst=[]

num=n
while num != k:
    if num % k == 0:
        lst.append(k)
        num/=k
    else:
        k+=1
lst.append(k)
exp=' * '.join(map(str,lst))
print(f'{str(n)} = {exp}')
print('%d = %s' %(n,exp)) #相同输出

