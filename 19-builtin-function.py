# # string funcation
# text="banana"
# print(text.count("a"))

# print("hello.py".endswith(".py"))
# print("hello.py".startswith("he"))
# print("123".isdigit())
# print("abc".isalpha())
# print("a123".isalnum())

# print("line1\nline2\nline3".splitlines())

# # list functions
# nums=[2,4,1,6,3]
# nums.sort()
# print(nums)

# fruits=["banana","apple","mango"] # if there is one small letter first all capital will come then small will come 
# print(sorted(fruits))

# marks=[10,20,30]
# print(min(marks),max(marks),sum(marks))

# mylist=[1,2,1,3,1]
# print(mylist.count(1))
# print(mylist.index(2)) # will give index of 2


# a=[1,2]
# b=[3,4]
# a.extend(b)
# print(a)

# # number function
# print(round(3.678,2))
# print(abs(-50))
# print(pow(3,4))
# print(divmod(10,3))
# print(sum([5,5,5],5))

# # practical examples
# products=[" mobile","laptop"," tablet"]
# clean=[p.strip().title() for p in products]
# clean.sort()
# # print(clean)

# email=["rohit@gmail.com","sneha@gmail.com"]
# domains=[mail[mail.find("@")+1:] for mail in email]
# print(domains)


# mobiles=["9898983456","8938984ff94","12345"]
# valid=[m for m in mobiles if m.isdigit() and len(m)==10]
# print(valid)


email=["rohit@gmail.com","sneha@gmail.com"]
domain=[]
for mail in email:
  domain.append([mail[mail.find("@")+1:]])
print(domain)  