
# file handling

# reading full file 
with open("20sample.txt","r") as f:
  print(f.read())
  
#reading line by line
with open("20sample.txt","r") as f:
  for line in f:
    print(line.strip().title())
    
# writing (overwrite)
with open("20notes.txt","w") as f:
  f.write("Day 20 - file handling\n")
  f.write("wrinting and reading")
    
# appending
with open("20notes.txt","a") as f:
  f.write("\nappending new line\n")
  
# cleaning data in file
cleaned=[]
with open("20sample.txt","r") as f:
  for line in f:
    cleaned.append(line.strip().title())
with open("20cleaned_output.txt","w") as f:   
  for city in cleaned:
    f.write(city+"\n") 
    

# counting lines
count=0
with open("20sample.txt","r") as f:
  for _ in f:  #_ means for each line
    count+=1
print("total lines ",count) 

   
 