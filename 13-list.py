# # list
# fruits=["apple","banana","orange"]
# print(fruits)
# print(fruits[0])
# print(fruits[-1])

# # update list
# fruits[1]="grapes"
# print(fruits)

# # addd items
# # fruits.append("mango")
# fruits.insert(1,"mango")
# print(fruits)

# # remove items
# fruits.remove("mango")
# fruits.pop(0)
# print(fruits)

# slicing
# nums=[10,20,30,40,50]
# print(nums[:3])
# print(nums[1:3])
# print(nums[-3:])
# print(nums[-3:-1])

# # looping
# fruits=["apple","banana","orange"] 
# for f in fruits:
#   print("fruit:",f)
  
  
#cleaning data 
# raw=["mUmbai","  DeLhi","pune "]
# clean=[]
# for c in raw:
#   clean.append(c.strip().title())
# print(clean)   


# replace wrong spellings
wrong=["kolkatta","Bengluru"]
fixed=[]
for c in wrong:
  c=c.replace("kolkatta","kolkata").replace("bengluru","bengaluru")
  fixed.append(c)
print(fixed)   


# extract years
codes=["laptop-2024","phone-2023"]
year=[]
for c in codes:
  year.append(c[-4:])
print(year)  
