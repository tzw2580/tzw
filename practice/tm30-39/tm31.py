'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''
d= {
    'm': '星期一',
    'w': '星期三',
    'f': '星期五',
    't': {'u': '星期二', 'h': '星期四'},
    's': {'a': '星期六', 'u': '星期日'}
}

first = input("请输入首字母：").strip().lower()[:1]
result = d.get(first)

if isinstance(result, dict):
    second = input("请输入第二个字母：").strip().lower()[:1]
    print(result.get(second, "无效的第二个字母"))
elif result:
    print(result)
else:
    print("无效的首字母")