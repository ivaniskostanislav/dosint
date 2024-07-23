import pandas as pd

# Sample data for df_cmts
data_cmts = {
    'PosterID': [1, 2, 3, 4, 5],
    'Comment': ['Comment A', 'Comment B', 'Comment C', 'Comment D', 'Comment E']
}

# Sample data for df_inf
data_inf = {
    'PosterID': [1, 3, 5],
    'Info': ['Info A', 'Info B', 'Info C']
}

# Creating DataFrames
df_cmts = pd.DataFrame(data_cmts)
df_inf = pd.DataFrame(data_inf)

print("Original df_cmts:")
print(df_cmts)

print("\nOriginal df_inf:")
print(df_inf)
