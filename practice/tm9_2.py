'''
模拟Linux用户登录。
验证账号和密码，若失败则延迟三秒输出错误信息。
'''
'''
题目：模拟Linux用户登录。
'''
import time
user = {'taozw': '5678',}
name='' # 全局变量预先定义
def login():
    global name # 声明使用全局变量name
    name = input('Username:')
    if name not in user:
        return False
    pswd = input('Password:')
    return user[name] == pswd

# 登录验证循环
while not login():  # 持续验证直到成功
    time.sleep(3)  # 失败后等待3秒（防暴力破解）
    print('Authentication failure') # 登录失败提示

# 模拟Linux终端提示符
print(name + '@localhost:~$') # 登录成功提示

