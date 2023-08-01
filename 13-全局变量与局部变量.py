# 用global修改全局变量
count = 10


def num1():
    count = 5
    print(count)


num1()
print(count)


def num2():
    global count
    count = 5
    print(count)


num2()
print(count)

# 用nonlocal解决函数嵌套中的变量关系


def x1():
    x = 5

    def x2():
        nonlocal x
        x *= x
        return x
    return x2()


print(x1())
