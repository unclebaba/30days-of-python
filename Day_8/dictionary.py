# Create an empty dictionary called dog
dog = {}
print(dog)

# Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'speedy',
        'color':'white',
        'legs':4,
        'breed':'chiwawa'}
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dict = {'first_name':'maryam',
            'last_name':'wambai',
            'gender':['female'],
            'age':21,
            'marital_status':'single',
            'skills':['project management', 'time management'],
            'country':'nigeria',
            'city':'kaduna',
            'address':{'street':'engineer street'}}
print(student_dict)

# Get the length of the student dictionary
print(len(student_dict))

# Get the value of skills and check the data type, it should be a list
print(student_dict['skills'])

# Modify the skills values by adding one or two skills
student_dict['skills'].append('python')
print(student_dict)

# Get the dictionary keys as a list
print(student_dict.items())

# Get the dictionary values as a list
keys = student_dict.keys()
print(keys)

# Change the dictionary to a list of tuples using items() method
list_tuples = list(student_dict.items())
print(list_tuples)

# Delete one of the items in the dictionary
del student_dict['skills']
print(student_dict)

# Delete one of the dictionaries
del student_dict['first_name']
print(student_dict)
