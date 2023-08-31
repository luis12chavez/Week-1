# 1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1-a
x[1][0] = 15
print(x)

# 1-b
students[0]["last_name"] = 'Bryant'
print(students[0])

# 1-c
sports_directory["soccer"][0] = 'Andres'
print(sports_directory["soccer"])

# 1-d
z[0]["y"] = 30
print(z)


# 2
def iterateDictionary(a_list):
    for i in a_list:
        # print(i)
        for key, val in i.items():
            print(key, "-", val)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 3
# print("\n")
def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4
print("\n")

def printInfo(some_dict):
    for key, val in some_dict.items():
        print("+++++++++++++++")        # added after solution watched
        print(len(val), key.upper())
        for i in range(0, len(val)):
            print(val[i])               # added after solution watched          
            # print(some_dict[key][i])

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
