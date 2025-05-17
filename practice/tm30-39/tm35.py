# 字符串常用操作
s='Hello world, I want to to my best.'
# 查找world
print(s.find('world'))
print(s.index('world'))

# 替换hello为hi
s_new=s.replace('Hello','Hi')
print(s,s_new)

n=s.count('o')
print(n)