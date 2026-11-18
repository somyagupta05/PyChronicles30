# clean customer names(strip+title)
import csv
cleaned_rows=[]
with open("22_sales_data.csv","r") as f:
  reader=csv.DictReader(f)
  
  for row in reader:
    row["Customer_Name"]=row["Customer_Name"].strip().title()
    cleaned_rows.append(row)
# print(cleaned_rows)    
with open("22cleaned_customer.csv","w",newline="") as f:
  writer=csv.DictWriter(f,fieldnames=reader.fieldnames)
  writer.writeheader()
  writer.writerows(cleaned_rows)
  
print("cleaned csv created: cleaned_customer.csv")  
  
