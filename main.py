import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Score': [85, 92, 78, 90, 88],
    'Course': ['Math', 'Science', 'History', 'Math', 'Science']
}

df = pd.DataFrame(data)
df

print(df.iloc[0])  # First row
print(df[['Name','Score']])  # Column name of second column
print(df['Course'].iloc[4]) # Course of the last row
