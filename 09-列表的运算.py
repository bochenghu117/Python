# 列表的比较：从第1组数开始比较，只要true了就是true
list1 = [123, 234]
list2 = [234, 123]
print(list1 < list2)
list3 = [123, 234]
print(list1 == list3)

# 列表的加法运算
list4 = list1 + list2
print(list4)

# 列表的翻转 reverse
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list5.reverse()
print(list5)

# 列表的从小到大排序 sort (会将字符串类型列表按首字母排列)
list6 = [1, 4, 78, 3, 56, 7, 12, 6]
list6.sort()
print(list6)

# 列表的从大到小排序 (会将字符串类型列表按首字母排列)
list6 = [1, 4, 78, 3, 56, 7, 12, 6]
list6.sort(reverse=True)
print(list6)

# 用len获得列表的长度(列表中元素的总数)
list7 = [1, 2, 3, 4, 5, 6]
print(len(list7))

# 用count获得列表中某元素出现的次数
list8 = [1, 1, 1, 1, 1]
print(list8.count(1))
