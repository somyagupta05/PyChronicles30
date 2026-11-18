# # dictionary
student={"name":"rohit","age":21,"city":"pune"}
# print(student)

# # accessing values
# print(student["name"])

# # adding and updating
# student["marks"]=85
# student["city"]="mumbai"
# print(student)

# # removing
# student.pop("age")
# print(student)


# # dictionary methods
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("name"))

# looping
for k in student:
  print(k,student[k])
  
# nested dictionary  
employees={
  "E101":{"name":"rohit","city":"pune"},
  "E202":{"name":"sneha","city":"mumbai"}
} 
print(employees["E101"]["name"])
  
  # mapping wrong -> coorect
mapper={
    "mombai":"Mumbai",  
    "kolkatta":"kolkata"  
  }
print(mapper["mombai"])