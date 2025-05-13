h=100
counts=1 # 落地次数
lst=[] #存放第i次落地的路程
while counts<=10:
    if counts == 1:
        lst.append(h)
        h/=2
        counts+=1
    else:
        lst.append(h*2)
        h/=2
        counts+=1
print(lst)
print('第10次落地时的总路程：',sum(lst))


