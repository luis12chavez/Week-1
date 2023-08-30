# 1
def count_down(int):
    new_list = []
    for i in range(int, -1, -1):
        new_list.append(i)
    return new_list

print(count_down(5))


# 2 
def print_return(li):
    print(li[0])
    return li[1]

print(print_return([1,2]))


# 3
def first_plus_length(li):
    sum = li[0]
    sum += len(li)
    return sum

print(first_plus_length([1,2,3,4,5]))


# 4 
def values_greater_than_second(li):
    new_list = []
    counter = 0
    # x = li[1]

    for i in range(0,len(li)):
        if len(li) < 2:
            return False
        elif li[1] < li[i]:
            counter+=1
            new_list.append(li[i])
    print(counter)
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


# 5 
def length_and_value(len,val):
    new_list = []
    for i in range(len, 0, -1):
        new_list.append(val)
    return new_list

print(length_and_value(4,7))
print(length_and_value(6,2))
