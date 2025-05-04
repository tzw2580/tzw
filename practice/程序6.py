# 题目：用 *号输出字母 C 的图案。
for i in range(6):
    if i == 0 or i == 5:
        print(' '+'*'*5)
    else:
        print('*'+' ')

def print_fancy_c(width, height):
    """打印带弧度的字母 C"""
    for row in range(height):
        if row == 0 or row == height - 1:
            print("*" * width)
        else:
            print("*" + " " * (width - 1))

# 示例：打印 6x5 的艺术化 C
# print_fancy_c(6, 5)