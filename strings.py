first_name = 'luis'
last_name = 'chavez'

# Two methods to String Interpolation
print("Format Method: Hello my name is {} {}" .format(first_name,last_name))

print(f"F-String Method: Hello my name is {first_name.capitalize()} {last_name.capitalize()}")

# comma and + methods
name = "Joe"
print ("My name is", name) # Adds a blank space by default
print("My name is " + name)

# changing type conversion
total = 35
user_val = "26"
# total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

# %-formatting: older method:
# %s - string
# %d - num
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

print("TEST!")



