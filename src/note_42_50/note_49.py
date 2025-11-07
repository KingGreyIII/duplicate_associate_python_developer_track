def call_to_print():
    print("This function is running smoothly")

def call_func_to_run(func_to_run):
    def trig_func():
        func_to_run()
    return trig_func

call_print = call_func_to_run(call_to_print)

def call_to_print():
    print("success")

call_print()

# # # original
def my_special_function():
    print('You are running my_special_function()')

def get_new_func(func):
    def call_func():
        func()

    return call_func

# Create a closure capturing the current my_special_function
new_func = get_new_func(my_special_function)

# Redefine my_special_function
def my_special_function():
    print("hello")

# Call new_func
new_func()
