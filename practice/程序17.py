s=input('字符串：')
letter=0
digit=0
space=0
others=0
for c in s:
    if c.isalpha():
        letter+=1
    elif c.isdigit():
        digit+=1
    elif c == ' ':
        space+=1
    else:
        others+=1

print(f'英文字母有{letter}个，数字有{digit}个，空格有{space}个，其他字符有{others}个。')
print('英文字母有{0}个，数字有{1}个，空格有{2}个，其他字符有{3}个。'.format(letter,digit,space,others))
print('英文字母有%s个，数字有%s个，空格有%s个，其他字符有%s个。' % (letter,digit,space,others))

