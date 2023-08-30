# 1
for i in range(151):
    print(i)

# 2
i = 5
while i <= 1000:
    print(i)
    i+=5

# 2a
# for i in range(5, 1005, 5):
#     print(i)

# 3
val = 1
while val <= 100:
    if val % 10 == 0:
        print("Coding Dojo")
    elif val % 5 == 0:
        print("Coding")
    else:
        print(val)
    val+=1

# 4
val = 0
total = 0
while val <= 500000:
    if val % 2 != 0:
        total += val
    val+=1
print(total)

# 5
for i in range(2018, 0, -4):
    print(i)

# 6
lowNum = 3
highNum = 20
mult = 4

while lowNum <= highNum:
    if lowNum % mult == 0:
        print(lowNum)
    lowNum+=1
