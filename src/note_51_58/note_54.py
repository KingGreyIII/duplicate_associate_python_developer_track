from functools import wraps
def html(open_tag, close_tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = func(*args, **kwargs)
            return '{}{}{}'.format(open_tag, msg, close_tag)

        # Return the decorated function
        return wrapper

    # Return the decorator
    return decorator


# Make hello() return bolded text
@html("<b>", "</b>")
def hello(name):
    return 'Hello {}!'.format(name)


print(hello('Alice'))