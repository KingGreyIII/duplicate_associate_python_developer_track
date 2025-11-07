# def multiply(a, b):
#     print(a * b)
#     return a * b
#
# def double_arg(func):
#     def wrapper(a, b):
#         # Double the arguments before calling the function
#         return func(a * 2, b * 2)
#     return wrapper
#
# # Create a new function that wraps multiply
# new_func = double_arg(multiply)
#
# new_func(3, 5)

def demo(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)


demo(10, 20, 30, name="Ryan", country="UK")

#  #  #
def print_before_and_after(func):
  def wrapper(*args):
    print('Before {}'.format(func.__name__))
    # Call the function being decorated with *args
    func(*args)
    print('After {}'.format(func.__name__))
  # Return the nested function
  return wrapper

@print_before_and_after
def multiply(a, b):
  print(a * b)

multiply(5, 10)