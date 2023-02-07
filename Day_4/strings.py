# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
sentence = 'thirty days of python'
print(sentence)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
sentence = 'Coding For All'
print('Coding For All')

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize()), print(company.title()), 

# Cut(slice) out the first word of Coding For All string.
cut_slice_coding = company[6:18] # starts at zero index and up to 3 but not include 3
print(cut_slice_coding)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print('Coding' in 'Coding For All')

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('coding', 'python'))

# Change Python for Everyone to Python for All using the replace method or other methods.
new_word = 'python for everyone'
print(new_word.replace('everyone', 'all'))

# Split the string 'Coding For All' using space as the separator (split()) .
challenge = 'Coding For All'
print(challenge.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
challenge = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(challenge.split(', '))

# What is the character at index 0 in the string Coding For All.
cut_slice_coding = company[-14:]
print(cut_slice_coding)

# What is the last index of the string Coding For All.
cut_slice_coding = company[13:] 
print(cut_slice_coding)

# What character is at index 10 in "Coding For All" string.
cut_slice_coding = company[10:] 
print(cut_slice_coding)

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
pte = 'Python For Everyone'

# Create an acronym or an abbreviation for the name 'Coding For All'.
cfa = 'Coding For All'

# Use index to determine the position of the first occurrence of C in Coding For All.
print(cfa.find("c,"))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(cfa.find("F,"))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(cfa.rfind("l,"))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
challenge = 'You cannot end a sentence with because because because is a conjunction'
sub_string_new = 'because'
print((challenge.index(sub_string_new)))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print((challenge.rindex(sub_string_new)))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
slice_because = challenge [0:25]
print(slice_because)

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sub_string_new = 'because'
print((challenge.index(sub_string_new)))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
slice_because = challenge [0:25]
print(slice_because)

# Does ''Coding For All' start with a substring Coding?
'yes'

# Does 'Coding For All' end with a substring coding?
'no'

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('coding for all',)

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
challenge = '30DaysOfPython'
print(challenge.isidentifier()) 
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) 

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' '.join(python_libraries)
print(result)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
#I just wonder what is next.
print("multiline string\nI am enjoying this challenge\nI just wonder what is next")

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("multiline string\tName Age Country City\tAsabeneh 250 Finland Helsinki")

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
result_new = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result_new) 

# Make the following using string formatting methods:
a = 8
b = 6
# 8 + 6 = 14
print(f'{a} + {b} = {a +b}')

# 8 - 6 = 2
print(f'{a} - {b} = {a - b}')

# 8 * 6 = 48
print(f'{a} * {b} = {a * b}')

# 8 / 6 = 1.33
print(f'{a} / {b} = {a / b:.2f}')

# 8 % 6 = 2
print(f'{a} % {b} = {a % b}')

# 8 // 6 = 1
print(f'{a} // {b} = {a // b}')

# 8 ** 6 = 262144
print(f'{a} ** {b} = {a ** b}')