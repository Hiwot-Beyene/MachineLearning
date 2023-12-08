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

print(pd.read_csv('data.csv'))
df1.to_csv('data.csv')

###pd.DataFrames.from_dict({})

#####Cleaning Empty cells 

#fillna and dropna


##### Working with Duplicates
# duplicates
# drop_duplicates

# df.drop_duplicates(
#     subset=None,            # Which columns to consider 
#     keep='first',           # Which duplicate record to keep
#     inplace=False,          # Whether to drop in place
#     ignore_index=False      # Whether to relabel the index
# )


sales = pd.read_csv('sales.csv')
targets = pd.read_csv('targets.csv')
print(sales.head())
print(targets.head())
sales_vs_targets = pd.merge(sales, targets)
print(sales_vs_targets)