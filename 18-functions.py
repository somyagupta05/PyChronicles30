# # functions
# def greet():
#   print("hello pyhton learners")
#   print("learning functions")
# greet()  

# def welcome(name):
#   print("welcome",name)
# welcome("somya")  

# # def add(a,b):
# #   print("a+b :",a+b)
# #   print("a*b :",a*b)
# # add(2,3)

# def add(a,b):
#   return a+b
# def multiply(x):
#   return x*2

# res=multiply(add(2,3))
# print(res)

# # cleaning
# def clean_text(value):
#   return value.strip().title()

# output=clean_text("  MuMbai")
# print(output)

# ,,,
# def fix_city(city):
#   city=city.lower().strip()
#   city=city.replace("mombai","Mumbai")
#   city=city.replace("kolkaataa","Kolkata")
#   return city.title()
# print(fix_city("mombai"))


# def get_year(code):
#   return(code[-4:])
# print(get_year("laptop-34543"))

# check validity
def isvalid_email(email):
  return '@' in email and "." in email
print(isvalid_email("test@gmail.com"))


def stats(num):
  return min(num),max(num),sum(num)/len(num)
print(stats([10,20,30]))


def clean_list(values):
  cleaned=[]
  for v in values:
    cleaned.append(v.strip().title())
  return cleaned 

print(clean_list([" delhi"," mumBai  ","PUNE "]))