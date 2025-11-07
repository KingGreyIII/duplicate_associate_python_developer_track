def my_special_function():
    print('You are running my_special_function()')


def get_new_func(func):
    def call_func():
        func()

    return call_func


# Overwrite `my_special_function` with the new function
my_special_function = get_new_func(my_special_function)

my_special_function()

# # # to run the last or recent update to my_special_func

def my_special_function():
    print('You are running my_special_function()')

def get_new_func():
    def call_func():
        # Instead of using a captured variable,
        # look up the latest global name each time.
        globals()['my_special_function']()
    return call_func

new_func = get_new_func()

# Redefine the function
def my_special_function():
    print("hello")

# Now this will reflect the new definition
new_func()
