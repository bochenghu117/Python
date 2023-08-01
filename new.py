def newfun():
    print("fun")

for i in range(100):    
    newfun()
    break
print("123321")

amount = 0
while i < 100:
    i = i + 1
    amount = amount + i
    print(amount)

print(amount)

print("--------------------------------------------------------------------------")

lit = [[1],[1,2],[1,2,3],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
for i in range(len(lit)):
    for j in range(len(lit[i])):
        print(lit[i][j])

print("--------------------------------------------------------------------------")


age = int(input("insert an age "))
if age > 5:
    print(">5")
elif age > 10:
    print(">10")
else:
    print("?")