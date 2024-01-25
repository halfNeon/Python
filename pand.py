import pandas as pd

'''#creating series
data=[12,56,3,38,79,70]
myseries=pd.Series(data)
print(myseries)

data={"Name":["abc", "xyz", "pqr"],
      "Age": [20,21,22],
      "City":["mumbai", "Pune", "Nashik"]}
df=pd.Series(data)
print(df)

#creating dataframe
data={"Name":["abc", "xyz", "pqr"],
      "Age": [20,21,22],
      "City":["mumbai", "Pune", "Nashik"]}
df=pd.DataFrame(data)
print(df)

#dataframe using list
data=[["abc", "xyz", "pqr"],
      [20,21,22],
      ["mumbai", "Pune", "Nashik"]]
df=pd.DataFrame(data, columns=("Name","Age","City"))
print(df)

#dataframe from csv file
df=pd.read_csv("C:/Users/admin/Desktop/annual-enterprise-survey-2021-financial-year-provisional-csv.csv ")
print(df)

#dataframe from excel file
#to create dataframe using excel intsall xlrd package (pip install xlrd)
df=pd.read_excel("C:/Users/admin/Desktop/file_example_XLS_10.xls ")
print(df)

#dataframe from json file
df=pd.read_json("C:/Users/admin/Desktop/dwsample2-json.json")
print(df)

#df excel file Analysis
df=pd.read_excel("C:/Users/admin/Desktop/file_example_XLS_10.xls ")
print(df.head(10))

df=pd.read_excel("C:/Users/admin/Desktop/file_example_XLS_10.xls ")
print(df.tail(6))

df=pd.read_excel("C:/Users/admin/Desktop/file_example_XLS_10.xls ")
print(df.info())

#add column in json file
df=pd.read_json("C:/Users/admin/Desktop/dwsample2-json.json")
add=["Mumbai","Hydrebad"]
df['Address'] = add
print(df)

#use dropna() to remove rows with any missing values
data = {
 'A': [1, 2, 3, None, 5], 
 'B': [None, 2, 3, 4, 5], 
 'C': [1, 2, None, None, 5]
}
df = pd.DataFrame(data)
print("Original Data:\n",df)
print()

df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)

data = {
 'A': [1, 2, 3, None, 5], 
 'B': [None, 2, 3, 4, 5], 
 'C': [1, 2, None, None, 5]
}
df = pd.DataFrame(data)
print("Original Data:\n",df)
print()

df_filled = df.fillna(0, inplace=True)
print("Cleaned Data:\n",df_filled)'''

data = {
 'A': [1, 2, 3, None, 5], 
 'B': [None, 2, 3, 4, 5], 
 'C': [1, 2, None, None, 5]
}
df = pd.DataFrame(data)
print("Original Data:\n", df)
# filling NaN values with 0
df.fillna(0, inplace=True)
print("\nData after filling NaN with 0:\n", df)
