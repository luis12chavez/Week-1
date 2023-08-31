# default parameters and named arguments
def func_greeting(name = "default", repeat = 2):
    print(f"Good Morning {name}!\n" * repeat)

func_greeting("Joe", 1)
func_greeting(repeat = 1, name = "Bill") # can pass as arguments as long as you define them by their parameter name