import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Score': [85, 92, 78, 90, 88],
    'Course': ['Math', 'Science', 'History', 'Math', 'Science']
}

df = pd.DataFrame(data)
df

# Filter students who passed (score >= 80)
passed_students = df[df['Score'] >= 80]
print(passed_students)

# Filter Science students
science_students = df[df['Course'] == 'Science']
print(science_students)

# Two conditions needs brackets
passed_science_students = df[(df['Score'] >= 80) & (df['Course'] == 'Science')]
print(passed_science_students)