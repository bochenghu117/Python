# @classmethod
# def 类方法名(cls):
#     pass

class tool(object):
    count = 0

    @classmethod
    def showcount(cls):
        print("数量为"+str(cls.count))

    def __init__(self, name):
        self.name = name
        tool.count += 1


tool1 = tool("11")
tool2 = tool("22")

tool.showcount()

# _new_的使用


class music(object):
    def __new__(cls, *args, **kwargs):
        # 创建对象时new方法会被自动调用
        print("创建对象，分配空间")
        # 为对象分配空间
        instance = super().__new__(cls)

        # 需要返回一个对象的引用
        return instance

    def __init__(self):
        print("初始化")


player = music()
print(player)
