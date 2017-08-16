import re

# 讲正则表达式编译成Pattern对象
patten = re.compile(r'hello.*\!')
match = patten.match('hello,zhangpan!How are you?')
print(match)
if match:
    print(match.group())


# 测试re.X(VerBOSE)
regex_1 = re.compile(r"""\d + # 数字部分
                         \.   #小数点部分
                         \d * #小数的数字部分""",re.X)

match = regex_1.match('4.300000.1415926')
if match:
    print(match.group(1, 2))


