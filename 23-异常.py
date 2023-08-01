# 最后一行的第一个单词就是错误类型
try:
    # 不能确定正确执行的代码
    num = int(input("输入整数"))
    result = 8/num
    print(result)
# 可以针对具体的错误类型来写代码
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("输入有效整数")
# 捕获未知错误(未提及的错误)
except Exception as result:
    print("未知错误"+result)
# 没有异常执行的代码
else:
    print("没有问题")
# 无论是否有异常都执行的代码
finally:
    print("结束")

# 使用raise主动抛出异常


def password():
    pwd = input("密码")
    if len(pwd) >= 8:
        return pwd
    # 创建异常对象
    ex = Exception("长度不够")
    # 抛出异常
    raise ex


try:
    print(password())
except Exception as result:
    print(result)
