# 集合不支持索引,集合会自动删除相同的元素,集合没有顺序
num = {1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 2, 1}
print(type(num))
print(num)

# 使用set创造集合
set1 = set([1, 2, 3, 4, 5, 5, 4, 3])
print(set1)

# 使用add与remove增加减少元素
set2 = set([1, 2, 3, 4, 5, 5, 4, 3])
set2.add(6)
print(set2)
set2.remove(1)
print(set2)

# 使用frozenset是集合不能被改变
set3 = frozenset([1, 2, 3, 4, 5, 5, 4, 3])
set3.add(5)
