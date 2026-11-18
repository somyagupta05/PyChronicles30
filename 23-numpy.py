# stores contiguous memeory unlike list
# 100x fatser than list
 
import numpy as np
print("creating arrays")
arr=np.array([10,20,30,40])
print(arr),

print("indexing and slicing arr ")
print(arr[1])

print("slicing array")
print(arr[0:2])

print("vectorized operation")
# in case of list will have to use loop 
print(arr+10)
print(arr*2)
print(arr**2)

print("numpy functions")
print(arr.sum())
print(arr.mean())
print(arr.min(),arr.max())

print("data cleaning")
data=np.array([10,-20,30,-40,50])
clean=data[data>=0]
print("cleaned",clean)

# missing number,
marks=np.array([80,90,-1,75,-1,60])
print("filles missing (-1) with avg value")
marks[marks==-1]=marks[marks!=-1].mean()
print(marks)

cities=np.array([" mumbai"," pUne","Delhi ","MUmbai"])
cities=np.char.strip(cities)
cities=np.char.title(cities)
print(cities)
