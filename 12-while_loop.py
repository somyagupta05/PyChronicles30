# while loop
# 1. basic while loop

# i=1
# while i<=5:
#   print(i)
#   i+=1
 
# #  2 countdown  
# n=5
# while n>0:
#   print(n)
#   n-=1

# ask until valid number
# num=""
# while not num.isnumeric():
#   num=input("enter any value")
#   print("please enter only num")
# print("accepted")  

# pritn list 
# items=["apple","banana","grapes","orange"]
# i=0
# while i<len(items):
#   print(items[i])
#   i+=1
  
  
# # using break   1 2 3 4 
# x=1
# while x<=10:
#   if x==5:
#     break 
#   print(x)
#   x+=1

# Continue will skip even 
y=0
while y<10:
  y+=1
  if y%2==0:
    continue
  print(y)
  
# password system
password=""
attempts=0

while password!="admin123" and attempts<3:
  password=input("enter password")
  attempts+=1
  if password=="admin123":
    print("login successful")
  else:
    print("wrong pass try again attempt count:",attempts)
    if attempts==3:
      print("3 attempts expired")
      