# 元组不可以被修改，但是可以使用列表的法则操作
y1 = (1, 2, 3, 4, 5)
print(y1)
print(y1[0])
print(y1[: 3])

# 强行修改元组
y2 = (1, 2, 4, 5, 6)
y2 = y2[:2]+(3,)+y2[2:]
print(y2)

# 把元组变成列表
y3 = (1, 2, 3, 4, 5, 6)
y3 = list(y3)
print(y3)
y4 = "i love you"
y4 = list(y4)
print(y4)

# 返回最大值(与ASCII码有关)
print(max(1, 2, 3, 4, 5, 6))

# 返回最小值(与ASCII码有关)
print(min("12345678"))

# enumerate与zip
num1 = [1, 2, 3, 4, 5, 6, 7]
num2 = [7, 6, 5, 4, 3, 2, 1]
list1 = list(enumerate(num1))
print(list1)
list2 = list(zip(num1, num2))
print(list2)

# 定义只包含一个元素的元组
tuple1 = (5,)
print(type(tuple1))

# 用count获得元组中某元素出现的次数
tuple2 = (1, 1, 1, 1, 1)
print(tuple2.count(1))

# 用index确定元素在元组中的位置(第一次出现)
print(tuple2.index(1))

# 用list将元组改为列表
tuple33 = (1, 2, 3)
list33 = list(tuple33)
print(type(list33))
