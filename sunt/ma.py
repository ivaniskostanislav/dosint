import pandas as pd

# Example DataFrame
data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 25, 30, 35]}
df = pd.DataFrame(data)

# Add a new column 'Marker'
df['Marker'] = ['Low', 'Medium', 'Medium', 'High', 'High']

print(df)
