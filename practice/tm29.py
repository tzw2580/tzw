# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
n=int(input('请输入正整数:'))
n_str=str(n)
while len(n_str) > 5:
    n = int(input('请重新输入正整数:'))
    n_str = str(n)
print(f'{n_str}是{len(n_str)}位数')
print('倒序输出：',n_str[::-1])