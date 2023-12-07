#panda data manupulation
# works with tabulara data
# data frame is an object that stores data as rows and cols
import pandas as pd
df1 = pd.DataFrame({
    'name': ['Smith', 'Jane', 'Joe'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
})
df2 = pd.DataFrame([
  [1, 'Indore', 100],
  [2, 'Bangalore', 120],
  [3, 'Hyderabad', 90],
  [4, 'Mumbai', 115]
],
  columns=[
    'ID', 'Location', 'Number of Employees'
  ])

print(df2)

print(df1)