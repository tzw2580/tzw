'''
题目：牛牛和牛妹一起玩密码游戏，牛牛作为发送方会发送一个4位数的整数给牛妹，牛妹接收后将对密码进行破解。
破解方案如下：每位数字都要加上3再除以9的余数代替该位数字，然后将第1位和第3位数字交换，第2位和第4位数字交换。
请输出牛妹破解后的密码。如1234-->6745.
'''
# 方法一
# n=int(input())
# lst=[]
# for i in str(n):
#     m=str((int(i)+3)%9)
#     lst.append(m)
# lst[0],lst[2]=lst[2],lst[0]
# lst[1],lst[3]=lst[3],lst[1]
# print(''.join(lst))

# 方法二
n=int(input())
gw=n%10
sw=n//10%10
bw=n//100%10
qw=n//1000
lst=[qw,bw,sw,gw]
for i in range(len(lst)):
    lst[i]=(lst[i]+3) %9
lst[0],lst[2]=lst[2],lst[0]
lst[1],lst[3]=lst[3],lst[1]
print(lst[0],lst[1],lst[2],lst[3],sep='')

