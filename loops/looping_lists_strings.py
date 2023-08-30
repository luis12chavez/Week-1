# for x in 'Hello':
    # print(x)  

# For-Loop through lists - with index
# ex_list = ["hello", 123, "Bye"]
# for index in range(0, len(ex_list)):
#     print(index, ex_list[index])

# For-Loop to get just the values(v)
# for v in ex_list:
#     print(v)

# While-Loop
count = 0
while count <= 5:
    print("Looping -", count)
    count+= 1

# else-statement
x = 3
while x > 0:
    print(x)
    x-=1
else:
    print("Final else statement" , x)

# break -  breaking out of a loop
for v in "string":
    if v == "i":
        break
    print(v)

# continue  statement is very useful when you want to skip specific iteration(s), but still keep looping to the end.
for v in "string":
    if v == "i":
        continue
    print(v)

# Conditionals: if-else
x = 55
if x > 10:
    print("Bigger than 10")
elif x > 50:
    print("Bigger than 50")
else:
    print("Smaller than 10")
