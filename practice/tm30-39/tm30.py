# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
# 方法一
n=int(input('请输入5位正整数:'))
while len(str(n)) != 5:
    n = int(input('请输入5位正整数:'))

gw=n%10
sw=n//10%10
qw=n//1000%10
ww=n//10000

if gw == ww and sw == qw:
    print(f'{n}是一个回文数！')
else:
    print(f'{n}不是一个回文数！')

# 方法二
num = str(int(input('输入数字：')))

# 判断是否为回文
def hw(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]: #前后索引对应的数相同
            return False
    return True
print('是否为回文数：', hw(num))

