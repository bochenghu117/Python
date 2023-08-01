# 用def创建函数
# def 函数名():
def FirstFunction():
    print("第一个函数")


FirstFunction()


def SecondFunction(name):
    print(name+" love you")


SecondFunction("i")


def ThirdFunction(age, gender):
    print("age is "+age+" gender is "+gender)


ThirdFunction("18", "male")

# 给函数提前定义、给函数默认值


def Function4(people="他", words="说你好"):
    print(people+words)


Function4()
Function4("你", "说逆天")

# 收集参数


def demo(*params):
    print("长度是：", len(params))
    print("第一个是：", params[0])


demo(1, 2, 3, 4, 5, 6, 7, 8, 9)


def h1():
    print(1)

    def h2():
        print(2)
    h2()


h1()

# 函数闭包


def x(x):
    def y(y):
        return x*y
    return y


print(x(3)(5))
