# tuples
fruits=("apple","banana","mango")
print(fruits)

# indexing
print(fruits[0])
print(fruits[-1])

# slicing
nums=(10,20,30,40,50)
print(nums[1:4])

# looping
colors=("red","blue","green")
for c in colors:
  print(c)

# tuple in length
print(len(colors)) 

# concatenation
a=(1,2)
b=(3,4)
print(a+b)

# pacing and unpacking
data=("laptop",4500,"black")
product,price,color=data
# print(product,price,color)
print(f"product :{product} price :{price} color :{color}")

# nested tuple inside list

employess=[("E101","Rohit","Pun"),("E102","Sneha","Mumbai")]
for eid,name,city in employess:
  print(eid,name,city)