import numpy as np
import pandas as pd

num_cols = 5
num_rows = 25
data_dict = {}

for col_num in range(1, num_cols + 1):
    arr = np.random.randint(low=1, high=100, size=num_rows)
    col_name = f"column_{col_num}"
    data_dict[col_name] = arr

df = pd.DataFrame(data_dict)
column_sums = df.sum().sort_values(ascending=False)
print(column_sums)
