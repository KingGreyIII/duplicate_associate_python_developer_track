def has_docstring(func):
    """Check whether the function `func` has a docstring."""
    return func.__doc__ is not None

def load_and_plot_data():
    """Loads and plots a dataset."""
    pass  # Pretend the body loads & plots data

ok = has_docstring(load_and_plot_data)

if not ok:
    print("load_and_plot_data() doesn't have a docstring!")
else:
    print("load_and_plot_data() looks ok")
