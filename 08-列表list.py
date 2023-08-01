# 列表可以包含任何格式
arr = [1, 1.003, "确实", [1, 2, 3], True, 3e47]
print(arr)

# 列表也可以是空列表
empty = []

# 用append向列表中添加元素(一次只能添加一个,在列表末尾)
arr.append("新增元素")
print(arr)

# 用extend向列表中添加元素(可以一次添加多个，用列表添加列表，在列表末尾)
arr.extend([5, 6, 7])
print(arr)

# 用insert插入元素(可以改变新元素的位置)
arr.insert(0, "第一位")
print(arr)

# 输出第几个值
print(arr[3])

# 用remove删除元素(也可以写列表中的具体元素)(会删除第一次出现的该元素)
arr.remove(5)
print(arr)

# 用del删除元素(del列表名将直接删掉整个列表)
del arr[0]
print(arr)

# 用pop删除元素(可以直接存在其他变量中)(如果pop里面没有参数，则会删去最后一个元素)
demo = arr.pop(2)
print(arr)
print(demo)

# 列表分片:列表名[a:b](从第a个开始，输出到第b个的前一个)可以只有a、只有b或只有：
print(arr[1:3])

# 用index确定元素在列表中的位置
print(arr.index(1))

# 用位置修改元素
arr[0] = 111
print(arr)

# 用clear清空列表
arr.clear()
print(arr)

# 用tuple将列表改为元组
list33 = [1, 2, 3]
tuple33 = tuple(list33)
print(type(tuple33))
