my_info = {
    "first": 'Luis', 
    "last": 'Chavez', 
    "age": 25,
    # "email": "test.com"
}
print(my_info["first"])

# Adding new key-value pairs
my_info["height"] = "5'7"   # can not have the same Key in a dict 
print(my_info["height"])

"""
# Testing if Key is in Dict
if some_key in my_dictionary:
    # update the value
"""
if "email" not in my_info:
    my_info["email"] = "testEmail.com"
else:
    print("Email key found already")

print(my_info["email"])

# Accessing values
full_name = my_info["first"] + " " + my_info["last"]
print(full_name)

# Removing Values
list2 = {
    "var" : 10,
    "var2" : 20
}

val_removed = list2.pop("var2")
del list2["var"] # will delete key, not return anything
print("Val Removed:", val_removed)
print(list2, "list2 is empty now")

# Built-in Functions and Methods
"""
len() - give the total length of the dictionary.
str() - produces a string representation of a dictionary.
type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dict type.
Here are some very useful Python dictionary methods:

.clear() - removes all elements from the dictionary
.get(key, default=None) - A safe way to get a value, if the key might not exist. Returns the value for the specified key or None (or a value you specify) if the key is not in the dictionary.
.update(pairs_to_update) - Add and update multiple key-value pairs at once, by passing in another dictionary of the pairs to update and add.

https://www.w3schools.com/python/python_ref_dictionary.asp
"""

print(my_info.get("weight"))
print(my_info)

print(type(my_info))

dic = {"key": 1, "key2": 2}
my_info.update(dic)
print(my_info)