'''
题目：将一个列表的数据复制到另一个列表中。
'''

origin = ['javascript', 'php', 'python']
refer = origin
copy = origin[:]  # origin.copy()

print('变量(%d): %s' % (id(origin), str(origin)))
print('引用(%d): %s' % (id(refer), str(refer)))
print('复制(%d): %s' % (id(copy), str(copy)))