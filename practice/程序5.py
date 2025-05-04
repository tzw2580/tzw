# 题目：输入三个整数x，y，z，请把这三个数由小到大输出。
# 方法一：sort或sorted
# sorted
# x,y,z=map(int,input('请输入三个数字（用空格隔开）：').split())
# num_sorted=sorted([x,y,z])
# print('从小到大排序：',num_sorted)
# sort
# num=list(map(int,input('请输入三个数字（用空格隔开）：').split()))
# num.sort()
# print('从小到大排序：',num)

# 方法二：条件判断
x,y,z=map(int,input('请输入三个数字（用空格隔开）：').split())
if x > y:
    x,y=y,x
if x > z:
    x,z=z,x
if y > z:
    y,z=z,y
print('从小到大排序：',x,y,z)