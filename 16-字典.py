# 字典没有顺序的概念
# dict = {键(keys):value},用键来寻找value
dict = {1: "First", 2: "Second", 3: "Third"}
print("第三个是：", dict[3])
print(dict[2])

# dict的改变
dict[2] = "第二个"
print(dict)

# dict的增加
dict[4] = "第四个"
print(dict)

# fromkeys的作用fromkeys((keys),(value))
dict1 = {}
print(dict1.fromkeys((1, 2, 3)))
print(dict1.fromkeys((1, 2, 3), ("one", "two", "three")))

for eachkey in dict1.keys():
    print(eachkey)

for eachValue in dict1.values():
    print(eachValue)

for eachItem in dict1.items():
    print(eachItem)

# get的使用
dict2 = {1: "First", 2: "Second", 3: "Third"}
print(dict2.get(1))
print(dict2.get(4))
print(dict2.get(1, "无"))
print(dict2.get(4, "无"))

print(1 in dict2)
print(4 in dict2)

# len的使用
print(len(dict))

# 用update合并字典
temp = {"height": 1.85}
zhangsan = {"name": "zhangsan"}
zhangsan.update(temp)
print(zhangsan)

# 清空字典
