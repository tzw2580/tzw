'''
题目：创建一个依次包含字符串'Niuniu'、'Niumei'、'GURR'和'LOLO'的列表current_users，
再创建一个依次包含字符串'GurR'、'Niu Ke Le'、'LoLo'和'Tuo Rui Chi'的列表new_users，
使用for循环遍历new_users，如果遍历到的新用户名在current_users中，
则使用print()语句一行输出类似字符串'The user name GurR has already been registered! Please change it and try again!'的语句，
否则使用print()语句一行输出类似字符串'Congratulations, the user name Niu Ke Le is available!'的语句。（注：用户名的比较不区分大小写）
'''
# 方法一：嵌套循环
current_users=['Niuniu','Niumei','GURR','LOLO']
new_users=['GurR','Niu Ke Le','LoLo','Tuo Rui Chi']
for i in new_users:
    for j in current_users:
        if i.lower() == j.lower():
            print(f'The user name {i} has already been registered! Please change it and try again!')
            break
    else: #注意else的位置：当内循环结束if都不满足，才会执行else
        print(f'Congratulations, the user name {i} is available!')

# 方法二
current_users_lower=[i.lower() for i in current_users]
for i in new_users:
    if i.lower() in current_users_lower:
        print(f'The user name {i} has already been registered! Please change it and try again!')
    else:
        print(f'Congratulations, the user name {i} is available!')
