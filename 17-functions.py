# # functions


# for i in range(1,6):
#   print(i)
  
# print("even num")
# for i in range(0,20,2):
#   print(i)
  
# print("odd num")
# for i in range(1,20,2):
#   print(i)  

# print("countdown")
# for i in range(10,0,-1):
#   print(i)  
  
items=["pen","book","cook"]
for i in range(len(items)):
  print(i,items[i])  
  
print("create year list")
years=[]
for y in range(2015,2026):
  years.append(y)
print(years) 

cities=[" mUmbai"," DelhI"," pUne"]
for i in range(len(cities)):
  cities[i]= cities[i].strip().title()
print(cities)  

# extract last 4 digits
ids=["emp-10203","ejk-18239","kdd-3678439"]
for i in range(len(ids)):
  print(ids[i][-4:])
  
for i in range(1,4):
  for j in range(1,4):
    print(f"i value:{i} j value:{j}" )  