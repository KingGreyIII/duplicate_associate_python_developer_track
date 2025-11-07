def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return func(*args, **kwargs)

    # Set count to 0 to initialize call count for each new decorated function
    wrapper.count = 0
    # Return the new decorated function
    return wrapper


# Decorate foo() with the counter() decorator
@counter
def foo():
    print('calling foo()')


foo()
foo()

print('foo() was called {} times.'.format(foo.count))
# my attempt
# def addition_func(func):
#     def wrapper(a, b):
#         addition_func = func(a * 2, b)
#
#         return addition_func
#     return wrapper
#
# @addition_func
# def foo(value):
#     return value
#
# print(foo(1, 2))