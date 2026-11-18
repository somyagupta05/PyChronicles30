import csv
# read entire csv
with open("21_sales_data.csv") as f:
  reader=csv.reader(f)
  for row in reader:
    print(row)

# read with ductreader
with open("21_sales_data.csv") as f:
  reader=csv.DictReader(f)
  for row in reader:
    print(row["Order_ID"],row["Customer_Name"],row["Payment_Type"])
    
# total sales
total=0
with open("21_Sales_data.csv") as f:
  reader=csv.DictReader(f)
  for row in reader:
    total+=int(row["Price"])*int(row["Quantity"])
print("Total Sales ",total)    
    
# filter by city
mumbai=[]
with open("21_sales_data.csv") as f:
  reader=csv.DictReader(f)
  for row in reader:
    if row["City"]=="Mumbai":
      mumbai.append(row)
print(mumbai)      


    