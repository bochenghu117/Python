# g = lambda x:2*x+1
def g(x): return 2*x+1


print(g(5))

# add = lambda x, y: x+y


def add(x, y): return x+y


print(add(3, 4))

# filter过滤器。会显示结果为True的元素
print(list(filter(None, [1, 0, True, False])))


def odd(x):
    return x % 2


range = range(10)
show = filter(odd, range)
print(list(show))
