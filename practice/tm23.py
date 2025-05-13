'''
题目：利用循环打印菱形
'''
#识别菱形的行数（必需是奇数）
row=int(input('请输入菱形的行数：'))
while row%2 == 0:
    print('请重新输入')
    row = eval(input('请输入菱形的行数：'))

top_row=(row+1)//2 #上半部分的行数，注意：top_row为int，必须是整除
#上半部分
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()
#下半部分
bottom_row=row-top_row #也可以row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,bottom_row*2-2*i+2): #1-->range(1,6), 2-->range(1,4), 3-->range(1,2)
        print('*',end='')
    print()