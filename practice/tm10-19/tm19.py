'''
题目：一个数如果恰好等于除了它以外的因子之和，这个数就称为“完数”。例如6=1＋2＋3。
编程找出1000以内的所有完数。
'''
for i in range(1,1000):
    sums=0
    for j in range(1,i):
        if i%j == 0:
            sums+=j
    if i ==sums:
        print(f'完数：{i}')
