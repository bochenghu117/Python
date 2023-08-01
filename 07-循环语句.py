# while循环
# which 条件：
#   循环语句
while 0 > 3:
    print("123")

# for循环
# for 目标 in 表达式
#   循环语句
arr = [1, 2, 3]
for i in arr:
    print(i)

demo = "demo"
for i in demo:
    print(i)

# range
# range([start,]stop[,step]) start代表起始数字，stop代表结束数字，step代表每step个数字记一次
for i in range(5):
    print(i)

for i in range(2, 9):
    print(i)

for i in range(2, 9, 3):
    print(i)

# break与continue
# break是跳出循环，continue是终止本次循环并开始下一次循环


# for循环与else的搭配使用
# 当for循环所有都执行完之后执行else里面的语句，除非有break
# 执行：
for i in [1, 2, 3]:
    print(i)
else:
    print("执行")

# 不执行：
for i in [1, 2, 3]:
    print(i)
    break
else:
    print("不执行")
