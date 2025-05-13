# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

poetry = input('五言绝句：')
print(reverse(poetry))