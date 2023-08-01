# 1 
# 输出100内所有奇数
# for i in range(100):
#     if i % 2 == 1:
#         print(i)
# print("-----------------------------------------------------------------------------------------------")

# 2 
# 输出1-100的和
# amount = 0
# for i in range(101):
#     amount = amount +i
# print(amount)
# print("-----------------------------------------------------------------------------------------------")

# 3
# 输出1-100所有质数
# for i in range(2,101):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#         else:
#             print(i)
#             break
# print("-----------------------------------------------------------------------------------------------")

# 4
# 判断一句话是否是回文
# word = input("输入想判断的内容")
# lis = []
# for i in range(len(word)):
#     lis.append(word[i])
# if lis == lis[::-1]:
#     print("yes")
# else:
#     print("no")
# print("-----------------------------------------------------------------------------------------------")

# 5
# 求两个数的最大公约数
# num1 = int(input("输入第一个数"))
# num2 = int(input("输入第二个数"))
# if num1 <= num2:
#     ind = 1
# else:
#     ind = 0
# if ind == 1:
#     for i in range(num1,1,-1):
#         if num1 % i == 0 and num2 % i == 0:
#             print(i)
# elif ind == 0:
#     for i in range(num2,1,-1):
#         if num1 % i == 0 and num2 % i == 0:
#             print(i)
# print("-----------------------------------------------------------------------------------------------")

# 6
# 求两个数的最小公倍数
# num1 = int(input("输入第一个数"))
# num2 = int(input("输入第二个数"))
# if num1 <= num2:
#     i = num2
#     while i > 0:
#         if i % num1 == 0 and i % num2 == 0:
#             print(i)
#             break
#         else:
#             i = i + 1
# else:
#     i = num1
#     while i > 0:
#         if i % num1 == 0 and i % num2 == 0:
#             print(i)
#             break
#         else:
#             i = i + 1
# print("-----------------------------------------------------------------------------------------------")

# 7
# 求两个数的和、差、商、积与余数
# num1 = int(input("输入第一个数"))
# num2 = int(input("输入第二个数"))
# print("和为" + str((num1 + num2)))
# print("差为" + str((num1 - num2)))
# print("商为" + str((num1 * num2)))
# print("积为" + str((num1 / num2)))
# print("余数为" + str((num1 % num2)))
# print("-----------------------------------------------------------------------------------------------")

# 8
# 输出100以内的所有偶数，直到累加和大于1000
# amount = 0
# for i in range(101):
#     if i % 2 == 0:
#         print(i)
#         amount = amount + i
#         if amount > 1000:
#             amount = amount -i
#             break
# print(amount)
# print("-----------------------------------------------------------------------------------------------")

# 9
# 计算一个字符串中有多少个单词
# count = 1
# sentence = input("输入一句话")
# for i in sentence:
#     if i ==" ":
#         count = count +1
# print(count)
# print("-----------------------------------------------------------------------------------------------")

# 10
# 计算一个列表中每个元素的平方
# lit = [1,2,3,4,5,6]
# for i in range(len(lit)):
#     lit[i] = lit[i] * lit[i]
# print(lit)
# print("-----------------------------------------------------------------------------------------------")

# 11
# 将一个列表中的元素去重
# lit = [1,1,1,2,3,4,5,6,6,6,7,8,9,9,9,9,9,0]
# lit2 = []
# lit2.append(lit[0])
# for i in lit:
#     for j in lit2:
#         if i in lit2:
#             break
#         else:
#             lit2.append(i)
# print(lit2)
# print("-----------------------------------------------------------------------------------------------")