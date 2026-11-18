# string methods
text1="    hello python learners     "

# remove spaces
print("original text:",text1)
print("remove spaces:",text1.strip())

# convert to capital
print("capital letter:",text1.upper())
# removing space together
print("capital letter:",text1.upper().strip())

# covert to proper case (first letter cap of every word)
print("capital letter:",text1.title().strip())

# lower case
print("capital letter:",text1.lower().strip())

# replace words
print("replace python with sql:",text1.replace("python","sql").strip())

# count occurrences of a letter of word
print("count of o",text1.count("o"))

# check if text start with something
print("start with hello:",text1.strip().startswith("hello"))

# check if only numbers are present in data
mobile="789839493sfd"
print("is numeric",mobile.isnumeric())

msg="wlecome to python course"

# split string into list of words
words=msg.split()
print("word list: ",words)

# join back with hyphen
joined_text="_".join(words)
print(joined_text)

# find position of letters
print("index of p:",msg.find("p"))



email="student@example.com"
domain=email[email.find("@")+1:]
print(domain)


 