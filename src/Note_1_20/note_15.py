import pandas as pd
result = []
for chunk in pd.read_csv("sales.csv", chunksize=1000):
    result.append(sum(chunk['x']))
result_sum = sum(result)
print(result_sum)