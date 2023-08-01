def demo(n):
    if n == 1:
        return 1
    else:
        return n * demo(n-1)


print(demo(5))
