# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# # 方法一
# from datetime import datetime
# from time import strptime
# date=input('请输入日期（格式为：YYYY-mm-dd）：')
# dt=strptime(date,'%Y-%m-%d')
# print(dt.tm_yday)

# 方法二：手动计算
# 思路：先判断平闰年，以2025年5月4日为例，平年，前4个月的天数和再加4天
# 判断平年or闰年
def is_leap_year(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        return True

def date(year,month,day):
    days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year):
        days_in_month[1]=29
    count_days=0
    for i in range(month-1):
        count_days+=days_in_month[i]
    count_days+=day
    return count_days

date_input=input('请输入日期（格式为：YYYY-mm-dd）：')
y,m,d=map(int,date_input.split('-'))
print(date(y,m,d))



