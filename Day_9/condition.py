# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output
age = input("Enter your age: ")
if age >= 18:
    print('You are old enough to drive')
    if age < 18:
        print('to wait for the missing amount of years')


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, 
# and a custom text if my_age = your_age. Output:        
my_age = 30
your_age = 25
if my_age > your_age:
    print('i am older')
else:
     print('your are older')

age = input("Enter your age: ")
if age > 0:
    if age % 25 == 5:
        print('age is 5 years difference')
    else:
        print('age is less than 5')
elif age == 5:
    print('5 years')
else:
    print('false')

# Get two numbers from the user using input prompt. If a is greater 
# than b return a is greater than b, if a is less than b return a is smaller than b, else a is equal to b. Output:
a = 4
b = 3
if a > b:
    print('a is greater than b')
elif a < b:
    print('b is smaller than')
else:
    print('a is equal to b')

### Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
A = 90-100, 
B = 70-89, 
C = 60-69, 
D = 50-59, 
F = 0-49, 
grade = input("Enter your grade: ")
if grade >= 90:
    print('Your grade is A')
else:
    if grade >= 80:
        print("Your grade is B")
    else:
        if grade >= 70:
            print("Your grade is C")
        else:
            if grade >= 60:
                print("Your grade is D")
            else:
                print("Your grade is F")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: 
# September, October or November, the season is Autumn. December, January or February, the season is C. 
# March, April or May, the season is Spring June, July or August, the season is Summer
season = input("Enter the month: ")
if season == 'September' 'October' 'November':
    print('Autumn')
else:
    if season =='December' 'January' 'February':
        print('Winter')
    else:
        if season == 'March' 'April' 'May':
            print('Summer')

# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
add_fruit=input('add a fruit into the list of fruit; ').lower()
if add_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(add_fruit)
    print(fruits)
  

person={
    'first_name': 'Joshua',
    'last_name': 'Samuel',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript','React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

    #Check if the person dictionary has skills key, 
    #if so print out the middle skill in the skills list.
if 'skills' in person:
    skills_length=len(person['skills'])
    if skills_length%2==0:
        middle_element=person['skills'][int(((skills_length/2)-1)) : int(((skills_length/2))+1)] 
        print('The middle element(s) :',middle_element)
    else:
        middle_element2=person['skills'][skills_length//2] 
        print('The middle element(s) :',middle_element2)

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill
# and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print(person['skills'])
    else:
        print('Not proficient in python')

#If a person skills has only JavaScript and React, print('He is a front end developer'),
#if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
# else print('unknown title') - for more accurate results more conditions can be nested!
if 'JavaScript' in person['skills'] and 'React' in person['skills']:
       print('He is a front end developer')
elif 'Node' in person['skills'] and 'python' in person['skills'] and 'MangoDB' in person['skills']:
    print('He is a backend developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MangoDB' in person['skills']:
    print('He is a fullstack developer')
else:
    print('Unknown title!')

 #If the person is married and if he lives in Finland, 
 # print the information in the following format:
if person['is_married']==True and person['country']=='Finland':
    print('{} {} is married. He lives in {}'.format(person['first_name'],person['last_name'],person['country']))
