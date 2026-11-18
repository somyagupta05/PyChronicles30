# if else conditioning

# age=int(input("enter your age:"))
# if age>18:
#   print("yes eligible")
# else:
#   print("not eligible")  
  
  
city="Delhi"
if city.lower()== "delhi":
  print("match")
else:
  print("not match")  
  

# will change input to lower case
password=input("enter your pass:")

if password.lower()=="admin@1":
  print("login successful")
else:
  print("wrong passsword")  
  
  
# email validation
email="user@example.com"
if '@' in email and "." in email:
  print("valid email")
else:
  print("invalid email")  