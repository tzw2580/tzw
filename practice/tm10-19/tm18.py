'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时，共有5个数相加)，几个数相加有键盘控制。
'''
# a=c=eval(input('请输入数字a：'))
# n=eval(input('请输入相加个数：'))
# lst=[]
# for i in range(n):
#     lst.append(c)
#     c=c*10+a
# print(lst)
# print(sum(lst))

# a=eval(input('请输入数字a：'))
# n=eval(input('请输入相加个数：'))
# terms=0
# lst=[]
# for i in range(n+1):
#     lst.append(terms)
#     terms=terms*10+a
# print(lst)
# print(sum(lst))

a=input('请输入数字a：')
n=eval(input('请输入相加个数：'))
terms=''
total=0
for i in range(1,n+1):
    terms+=a
    total+=int(terms)
print(total)

