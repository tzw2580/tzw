'''
题目：打印出所有的“水仙花数”.所谓“水仙花数”是指一个三位数，
其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
'''
# 方法一
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i**3+j**3+k**3 == 100*i+10*j+k:
                print(i,j,k,sep='')

# 方法二
for n in range(100,1000):
    gw=n%10 #个位
    sw=n//10%10 #十位
    bw=n//100 #百位
    if gw**3+sw**3+bw**3 == n:
        print(bw,sw,gw,sep='')
