import pandas as pd
import numpy as np

# Read a CSV file into a DataFrame
df = pd.read_csv("pandas_hidden_hunt.csv")

# Display secret star student that studies Computing and has submitted their project, has an attendance percentage of 90 or above, studies 6 or more hours per week, has an exam score of 85 or above, and has the highest exam score among such students.
secret_star_student = df[(df['Course'] == 'Computing') & (df['ProjectSubmitted'] == 'Yes') & (df['AttendancePercent'] >= 90) & (df['StudyHoursPerWeek'] >= 6) & (df['ExamScore']  >= 85)]
secret_star_student = secret_star_student.loc[secret_star_student['ExamScore'].idxmax()]
print(secret_star_student)
