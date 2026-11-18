# used for manipulation and analysis
# like microsoft excel but 1000x fatser than excel
# panel+data=pandas

import pandas as pd
# load csv file 
df=pd.read_csv("24employeedata.csv")
# print("raw data")
# # print(df.head()) #top 5 rows
# # print(df) #full data
# # print(df.head(10))
# # print(df.head(-30))

# # print(df.tail(5))

# # basic info
# print("Shape",df.shape)
# print("columns",df.columns)
# print(df.info())
print(df.describe())
# # clean text data
# # clean emlpoyee name
# df["Employee_Name"]=df["Employee_Name"].str.strip().str.title()
# print(df.head)

# # clean city name
# df["City"]=df["City"].str.strip().str.title()
# print(df.head())

# # clean department
# df["Department"]=df["Department"].str.strip().str.title()
# print(df.head())

# # cleaned data
# print("cleaned data")
# print(df[["Employee_Name","City","Department"]].head())

# remove duplicates
# print("dulpicate rows",df.duplicated().sum())
# df=df.drop_duplicates()
# print(df)

# # filter data
# # employees from mumbai
df["City"]=df["City"].str.strip().str.title()
mumbai_emp=df[df["City"]=="Mumbai"]
# print(mumbai_emp.head())
mumbai_emp.to_csv("24Mumbai_emp.csv",index=False)

# # employess with slary >60000
high_sal=df[df["Salary"]>65000]
print(high_sal)

# writing 0 to show rows and 1 to show column
print("employees with salary >60000",high_sal.shape[0])

# sort data
# sort by salary(descending)
df_sorted_sal=df.sort_values("Salary",ascending=True)
print(df_sorted_sal.head())

# sort by joining year
df_sorted_year=df.sort_values("Joining_Year",ascending=False)
print(df_sorted_year.head())

# add new columns
# salary category
df["Salary_Category"]=df["Salary"].apply(lambda x: "High" if x>=60000 else "Medium" if x>=50000 else "Low")
print(df.head())

# experience (years)
df["Experience"]=2025-df["Joining_Year"]
print(df.head())

# group by operations
# average sal by dept
avg_Sal_dept=df.groupby("Department")["Salary"].mean()
print(avg_Sal_dept)

# total salary by city
df["City"]=df["City"].str.strip().str.title()
total_sal_city=df.groupby("City")["Salary"].sum()
print(total_sal_city)

# employee count by dept
count_dept=df.groupby("Department")["Employee_ID"].count()
print(count_dept)

# export cleaned data -sort by salary(descending)
df_sorted_salary=df.sort_values("Salary",ascending=False)
df_sorted_salary.to_csv("24employee_sorted_by_salary.csv",index=False)
