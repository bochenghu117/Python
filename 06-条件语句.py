# 在python中，else if写作elif
count = 3
while count > 0:
    score = int(input("输入成绩"))
    if score >= 70 and score <= 100:
        print("A")
    elif score < 70 and score >= 60:
        print("B")
    elif score < 60 and score >= 50:
        print("C")
    elif score < 50 and score >= 40:
        print("D")
    elif score < 40 and score >= 0:
        print("E")
    else:
        print("ERROR")
