# 1. text data type
customer="somya"
print("name is",customer)
print("type is",type(customer))


# 2. numeric datatype
# 2.1 integer
rate=3
print("type is",type(rate))


# 2.2 float-decimal num
rangee=34.45
print("type is",type(rangee))

#  2.3 complex number
a=3+4j
print("type is",type(a))

# 3. boolean
is_paid=True
print("type is",type(is_paid))

# 4.sequence 
# 4.1 list
listt=["mum",123,"som"]
print(listt)
print(type(listt))

# 4.2 tuple
tup=("som",12)
print(tup)
print(type(tup))

# 4.3 range
num=range(1,11)
print(list(num))
print(type(num))

# 5 dictionary
student={
  "name":"Anvi",
  "age":5,
  "city":"mumbai"
}
print(student)
print(type(student))

# 6. set
numbers={1,2,2,3,4}
print(numbers)

# 7.None type - no value
remarks=None
print(remarks,type(remarks))