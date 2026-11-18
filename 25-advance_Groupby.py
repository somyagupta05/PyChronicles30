import pandas as pd
# load cleaned employee data
df=pd.read_csv("24employeedata.csv")
print("data loaded")
print(df.head())

# filtering
# employees from mumbai
df["City"]=df["City"].str.strip().str.title()
mumbai_emp=df[df["City"]=="Mumbai"]
print(mumbai_emp)

# high salary emp
high_Sal=df[df["Salary"]>60000]
print(high_Sal)

# multiple conditions
mumbai_high=df[(df["City"]=="Mumbai")&(df["Salary"]>60000)]
print(mumbai_high)

# using isin()
IT_and_Finance=df[df["Department"].isin(["IT","Finance"])]
print(IT_and_Finance)

# advanced sorting
# sort by salry desc
df_sorted_Sal=df.sort_values(["Salary"],ascending=False)

# sort by dept then salary
df_sorted_multi=df.sort_values(["Department","Salary"],ascending=[True,False])
print(df_sorted_multi)

# group by operatiions
# average sal by dept
avg_Sal_dept=df.groupby("Department")["Salary"].mean()
print(avg_Sal_dept)

# # total salary by city
# df["City"]=df["City"].str.strip().str.title()
# total_sal_city=df.groupby("City")["Salary"].sum()
# print(total_sal_city)

# # employee count by dept
# count_dept=df.groupby("Department")["Employee_ID"].count()
# print(count_dept)

# multiple aggregations
salary_stats=df.groupby("Department")["Salary"].agg(["min","max","mean","count"])
print("salary stats")
print(salary_stats)

# sort groupby
sorted_avg_salary=avg_Sal_dept.sort_values(ascending=False)
print("dpartment by avg salary")
print(sorted_avg_salary)