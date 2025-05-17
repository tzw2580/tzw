'''
题目：压缩字符串。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
比如，字符串aabcccccaaa会变为a2bc5a3.
'''
def fun(s:str):
    result=[]
    s1=s[0] # 迭代记录第一个新出现的元素
    count=1
    for i in s[1:]:
        if i == s1:
            count+=1
        else:
            result.append(s1)
            if count > 1:
                result.append(str(count))
            count=1
            s1=i
    # 处理最后一个字符
    result.append(s1)
    if count > 1:
        result.append(str(count))

    return ''.join(result)
print(fun('aaabbccc'))
print(fun('aabcccccaaaa'))

