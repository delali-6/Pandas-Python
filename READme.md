print(df.head()) #first five rows
print(df.tail()) #last 5 rows
print(df.shape) #rows and columns
print(df.columns) #column names
print(df.info()) #data types and missing values
print(df.describe()) #numeric summary

# Filter students who passed (score >= 80)
passed_students = df[df['Score'] >= 80]
print(passed_students)

# Filter Science students
science_students = df[df['Course'] == 'Science']
print(science_students)

# Two conditions needs brackets
passed_science_students = df[(df['Score'] >= 80) & (df['Course'] == 'Science')]
print(passed_science_students)

print(df["Name"])

print(df['Score'] >= 80)