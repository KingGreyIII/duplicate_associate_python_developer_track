from functools import wraps  # <-- important import

def tag(*tags):
    # Define a new decorator
    def decorator(func):
        # Ensure the decorated function keeps its metadata
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Call the function being decorated and return the result
            return func(*args, **kwargs)
        # Attach custom attribute "tags" to the wrapper
        wrapper.tags = tags
        return wrapper
    # Return the decorator
    return decorator


@tag('test', 'this is a tag')
def foo():
    pass

print(foo.tags)
