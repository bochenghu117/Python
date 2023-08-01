class cat:
    def __init__(self, name):
        print("初始化方法")
        # self.属性名 = 属性初始值
        self.name = name

    # 必须有一个返回值，会输出自定义信息
    def __str__(self):
        return "我是"+self.name

# 类的私有属性与私有方法，在外界不能被访问与调用


class siyou:
    def siyou(self):
        self._num = 100

    def _siyou(self):
        print("私有方法")


# 当使用类名()创建对象的时候，会自动调用初始化方法
tom = cat("Tom")
lazycat = cat("lazycat")
print(tom.name)
print(lazycat.name)
print(tom)
print(lazycat)

# 类的继承写法(子类拥有父类所有属性及方法)(子类可以有多个父类,用,分割)
# 原理是子类(父类)


class animal:
    def eat(self):
        print("吃")

    def fly(self):
        print("慢")

    def bark(self):
        print("小声叫")


class demo:
    def nihao(self):
        print("你好")


class dog(animal, demo):
    def drink(self):
        print("喝")

# 在子类中重写父类的方法，会覆盖父类的方法

    def fly(self):
        print("快")

# 用super()调用原本在父类中的方法

    def bark(self):
        print("大声叫")
        super().bark()


dahuang = dog()
dahuang.eat()
dahuang.drink()
dahuang.fly()
dahuang.bark()
dahuang.nihao()
