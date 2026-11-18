# for loop
# 1. basic loop

# for i in range(1,10):
#   print(i)


# 2 print characters
# word="python"
# for alphabet in word:
#   print(alphabet)

# word="sql"
# for i in range(1,11):
#   print(word)

# items=["pen","book","tea","coffee"]
# for item in items:
#   print(item)  
  
# # even number
# for n in range(0,20,2):
#   print(n)
  
# # odd number
# for n in range(1,21,2):
#   print(n)
  
# print sum  
marks=[23,23,45]
total=0
for m in marks:
  total+=m
print(total) 


# clean city names
cities=[" mumbai","pune "," chennai"]
cleaned=[]
for c in cities:
  cleaned.append(c.strip().title())
print(cleaned)  

# loop with if
nums=[12,23,25,5,9,7]
for n in nums:
  if n<10:
    print(n,"is smaller than 10")
  else:
    print(n,"is greater than 10")  
 
# extract last digits from ids
ids=["emp-001122","emp-889900"]
for last4 in ids:
  print(last4[-4:])