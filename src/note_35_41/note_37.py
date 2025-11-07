# score = [2, 3, 4, 1,2, 1]
# def median(score_sheet):
#   """Get the median_func of a sorted list of score_sheet
#
#   Args:
#     score_sheet (iterable of float): A list of numbers
#
#   Returns:
#     float
#   """
#   # Write the median_func() function
#   score_sheet = sorted(score_sheet)
#   midpoint = int(len(score_sheet) / 2)
#   if len(score_sheet) % 2 == 0:
#     median_func = ((score_sheet[midpoint - 1] + score_sheet[midpoint])/2)
#   else:
#     median_func = score_sheet[midpoint]
#   print(median_func)
# median(score)
#
# a = [2, 3, 4,4 ,4, 2, 1]
# a[0] = 100
# a.pop(4,4, 4)
# print(a)

import pandas as pd

def better_add_column(values, df=None):
    """Add a column of `values` to a DataFrame `df`."""
    if df is None:
        df = pd.DataFrame()        # Create new DataFrame only if none was given
    df['col_{}'.format(len(df.columns))] = values
    return df

# Example
df1 = better_add_column([1, 2, 3])
df2 = better_add_column([4, 5, 6])

print(df1)
print(df2)
