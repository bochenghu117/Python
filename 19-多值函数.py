# *参数：接收元组
# **参数：接收字典
def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


# 注释demo(1)结果会不同
demo(1)
demo(1, 2, 3, 4, 5, name="张三", age=18)
