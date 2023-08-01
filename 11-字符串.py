# format的使用
print("{0} love {1}".format("i", "you"))
print("{a} love {b}".format(a="i", b="you"))
print("{0} love {b}".format("i", b="you"))

# 在遇到使用双引号的时候用单引号定义
str1 = '我是"47"'
print(str1)

# 字符串索引字符
str2 = "abcdefg"
print(str2[0])

# 用len统计字符串长度
print(len(str2))

# 用count统计小字符串出现的次数
print(str2.count("a"))

# 用index获得字符串出现的位置
print(str2.index("e"))

# 字符串的切片(每隔n个)(字符串名[::n])
str3 = "12345678"
print(str3[::2])

# 字符串的切片(从a开始到b个每隔n个)(字符串名[a:b:n])
str3 = "12345678"
print(str3[1::2])

# 获得最后一个字符
print(str3[-1])

# 获得最后两个
print(str3[-2:])

# 倒序切片
print(str3[-1::-1])
