import re
 
#Due: February 11th at the beginning of class

#Name: Shyan Yen

                                    # Lab 2

# Each of the sentences below are followed by a set of related instructions.
# After each instruction, add your code that does what's being asked, as well as
# a print statement that shows your work. Don't forget to print new lines as well,
# or your output will be a mess!

# 1) Write a regular expression and if statement that checks if T is the first letter

pattern = r"T"
print("1)")
s0 = "Today is a new day"
print("Statement 1 is " + "'" + s0 + "'")
print("The output will show if the beginning of the sentence starts with capital T:" + "\n")
if re.match(pattern, s0):
    print ("Match, it starts with a T." + "\n")
else:
    print ("My regex is incorrect, it should detect the 'T'!" + "\n")

# 2) Use a regular expression to decompose the string into words and place those words into a list.
#    Extract the first word into a variable and print it

pattern = "\s+"
t0 = 'My dog just spilled the juice'
print('-----------------------------------------------------------------------------')
print("2)")
print("Statement 2 is " + "'" + t0 + "'")
print("The output will show a list of words within the statement and first word:")
words = re.split(pattern, t0)
print("\n")
print("Here is the list of words:")
print(words)
first_word = words[0]
print ("The first word is: '" + first_word + "'\n")
print('-----------------------------------------------------------------------------')

# 3) Split the sentence into an array of individual words called words and use a for loop to print it.

print("3)")
pattern = "\s+"
t1 = "I am going to buy myself a coffee"
print("Statement 3 is " + "'" + t1 + "'")
print("The output will split the sentence into individual words and print it:" + "\n")
words = re.split(pattern, t1)
for word in words:
    print(word + "\n") 

print('-----------------------------------------------------------------------------')

# 4)
# a) Write a regular expression and if statement that checks if the name "Mary" in the sentence.

print("4)")
s1 = "Mary was born on September 17, 1986" 
print("Statement 4 is " + "'" + s1 + "'")
pattern = r"Mary*"
print("The output will show if Mary is in the sentence above: " + "\n")
if re.match(pattern, s1):
    print ("Match, Mary is in the sentence." + "\n")
else:
    print ("My regex is incorrect, it should detect 'Mary'!" + "\n")
    
# b) Write a regular expression and if statement that checks if the sentence contains a 4 digit number.

pattern = r'\d'
fourDigits = re.findall(r"\b\d{4}\b", s1)
print("The next ouput will show if a 4 digit number is in the sentence:" + "\n")
if re.findall(r"\b\d{4}\b", s1):
    print ("Match, there is a 4 digit number in the sentence." + "\n")
    print ("Here are the digits:")
    print (fourDigits)
else:
    print ("My regex is incorrect, it should detect a 4 digit number!" + "\n")
    
# c) Write a regular expression to extract that number into a variable b_year and print it in this sentence:
#    "The person was born in b_year."

print("\n")
b_year = ''.join(fourDigits)
print ("The person was born in the year " + b_year + "." + "\n")
print('-----------------------------------------------------------------------------')

# 5)
print("5)")
s2 = "The dog, named Dog, was doggedly trying to dodge the fog."
print("Statement 5 is '" + s2 + "'" + "\n")

# a) Write a regular expression to match the word "dog", but not the name "Dog"

print("This will match the word 'dog' with case sensitivity:" + "\n")
pattern = re.compile(r'\bdog\b')
matches = pattern.finditer(s2)

for match in matches:
    print(match)
    dogOnlyList = pattern.finditer(s2)
    print(dogOnlyList)
    print("\n")
    
# b) Save the output from this match into a list and print the list to verify it is not matching anything else.

print("This will print out the list of 'dog' only:")
pattern = r'\bdog\b'
if re.findall(pattern,s2):
    dogOnlyList = re.findall(pattern,s2)
    print(dogOnlyList)
    print("\n")
else:
    print('This regex is wrong Shy')
    
# c) Write a regular expression to match "dog" and "Dog" using a flag (see the cheat sheet).

print("This will match the 'dog' and 'Dog' string using a flag and print the match:" + "\n")
pattern = re.compile(r'dog', flags = re.LOCALE)
matches = pattern.finditer(s2)
for match in matches:
    print(match)
print("\n")

# d) Write a regular expression to match "dog" or "fog"

print("This will match 'dog' or 'fog' and print the match:" + "\n")
pattern = re.compile(r'\bdog|fog\b')
matches = pattern.finditer(s2)
for match in matches:
    print(match)
print("\n")
# e) Print all outputs.
print('-----------------------------------------------------------------------------')

# 6)
# a) Write a regular expression to extract the first number (try to do it without using the exact string).

print("6)")
s3 = "18785 is the 5 digit number I want not 43744, 34553, or 11111"
print("Statement 6 is '" + s3 + ".'" + "\n")
if re.findall(r"\b\d{5}\b", s3):
    fiveList = re.findall(r"\b\d{5}\b", s3)
    print("Extracting first number: ")
    print(fiveList[0])
    print("\n")
else:
    print("You did not do the correct regex Shy")
    
# b) Write a regular expression to extract all numbers, store them in an array, then print the array.

if re.findall(r"\b\d{5}\b", s3):
    fiveList = re.findall(r"\b\d{5}\b", s3)
    print("Array of numbers in the statement: ")
    print(fiveList)
    print("\n")
print('-----------------------------------------------------------------------------')

# 7) Write a regular expression to trim the left and right whitespace and print the trimmed output.

print("7)")
s4 = "    There is preceding white space in this sentence, and whitespace at the end        "
print("Statement 7 is '" + s4 + "'" + "\n")
newS = re.sub("^\s+|\s+$", "", s4, flags=re.UNICODE)
print("New statement removing whitespace: ")
print("'" + newS + "'" + "\n")
print('-----------------------------------------------------------------------------')

#8)
# a) Write a regular expression to print everything from the first "begin" to the last "end".

print("8)")
s5 = "junk data penguin begin tennis for 2 end begin Zelda and Link end begin Oculus Rift end no cheating by using " \
     "positional text flags"
     
print("Statement 8 is '" + s5 + "'" + "\n")
print("Work shown: ")
x = re.split("begin", s5)

print(x)

sentence = ""

for i in range (1,len(x)):
    sentence += "begin" + x[i]

print(sentence)

x = re.split("end",sentence)

print(x)

sentence = ""
print("\n")

print("This will print the final sentence:")

for i in range (0,len(x)-1):
    sentence += x[i] + "end"

print(sentence)
print("\n")

# b) Write a regular expression to print only the text from the first "begin" to the first "end"

x = re.split("begin", s5)
print("Work shown:")
print(x)

sentence = "" 

for i in range (1,len(x)):
    sentence += "begin" + x[i]

print(sentence)

x = re.split("end",sentence)

print(x)

sentence = ""
print("\n")

print("This will print the final sentence:")

for i in range (0,1):
    sentence += x[i] + "end"

print(sentence)
print("\n")

# c) Write a regular expression to extract all of the text between "begin"s and "end"s into an array.
print("This will extract all text between the begin's and end's and form an array:")
x = re.split("begin", s5)

# print(x)

sentence = ""

for i in range (1,len(x)):
    sentence += x[i]

#print(sentence)

x = re.split("end",sentence)
x.pop(len(x)-1)
print(x)

# d) Print all outputs.
print('-----------------------------------------------------------------------------')
# 9)
s6 = "The date 5/17/1982 is trickier to get"

# a) Write a regular expression to extract the date.
# b) Capture the date in a variable f_date
print("Statement 9 is '" + s6 + "'")
print("Here is part A and B:")
x = re.split('\s+', s6)
#print(x)
f_date = ""

for word in x:
    y = re.findall('\d', word)
    if(y):
        f_date = word
print(f_date)
print("\n")

# c) Split the date and store it as month, day, year
print("Here is part C: ")
x = re.split('/',f_date)
month = x[0]
day = x[1]
year = x[2]
print("Month: " + month)
print("Day: " + day)
print("Year: " + year + "\n")

# d) Convert the date to date format year-month-day where month and day always have 2 digits. Save the 
#    result in comp_date 5/17/1982
x = re.split('/',f_date)
month = x[0]
day = x[1]
year = x[2]
if len(month) <2:
    month = "0" + month
if len(day) <2:
    day = "0" + day
comp_date = year + "-" + month + "-" + day
print("This will convert the date to fit the year-month-day format:")
print(comp_date)
    
# e) Print comp_date

print('-----------------------------------------------------------------------------')


