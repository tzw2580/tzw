# 题目：输入两个数，分别输出按位与&、按位或|、按位异或^、按位取反~运算的结果。

a,b=map(int,input('请输入两个整数：').strip().split())
print('位与',a & b)
print('位或',a | b)
print('位异或',a ^ b)
print('位取反',~a,~b)

