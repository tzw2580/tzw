# 题目：输出 9*9 口诀表。
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={i*j:>2}',end='    ') # 结果右对齐
    print()

