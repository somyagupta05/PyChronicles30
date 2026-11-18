# sets
# create set
fruits={"apple","banana","apple","mango"}
print(fruits)

# add item  will be added any where as it is unordered
fruits.add("orange")
print(fruits)

# remove items
fruits.discard("banana")
print(fruits)

# set operations
a={1,2,3}
b={3,4,5}
print("union:",a|b)
print("intersection",a&b)
print("diferences",a-b)
print("symmetric difference",a^b) #will not show items present in both

# # remove duplicates
# cities=["mumbai","pune","delhi","mumbai"]
# unique=set(cities)
# print("unique cities ",unique)

# missing values
list1={"sql","excel","powerbi"}
list2={"sql","powerbi"}
missing=list1-list2
print(missing)

# common skills
list1={"sql","excel","python"}
list2={"excel","python","powerbi"}
print("common: ",list1&list2)
