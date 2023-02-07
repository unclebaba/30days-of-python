# Declare an empty list
empty_list = list() 
print(len(empty_list))


# Declare a list with more than 5 items
country = ['nigeria', 'togo', 'canada', 'usa', 'australia'] 

#Find the length of your list
print('country:', len(country))

# Get the first item, the middle item and the last item of the list
first_country = country[0]
print(first_country)
middle_country = country[2]
print(middle_country)
last_country = country[4]
print(last_country)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = 'baba, 29, 1.72, single, male, kaduna'
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon'

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print('number of it_companies:', len(it_companies))

# Print the first, middle and last company
first_com = it_companies[0]
middle_com = it_companies[3]
last_com = it_companies[6]
print(first_com)
print(middle_com)
print(last_com)

# Print the list after modifying one of the companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' 'Amazon']
it_companies[0] = 'Whatsapp'
print(it_companies)

# Add an IT company to it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' 'Amazon']
it_companies.append('Snapchat')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Twitter')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)




# Join the it_companies with a string '#;  '
print(str(it_companies))


# Check if a certain company exists in the it_companies list.
does_exist = 'Facebook' in it_companies
print(does_exist)


# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_3_companies = it_companies[4:]
print(first_3_companies)

# Slice out the last 3 companies from the list
last_3_companies = it_companies[0:3]
print(last_3_companies)

# Slice out the middle IT company or companies from the list


# Remove the first IT company from the list
it_companies.remove('Facebook')
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.remove('IBM')
print(it_companies)

# Remove the last IT company from the list
it_companies.remove('Twitter')
print(it_companies)

# Remove all IT companies from the list
it_companies.remove('Snapchat')
print(it_companies)

# Destroy the IT companies list
it_companies.clear()
print(it_companies)

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux' + 'Node','Express', 'MongoDB']
print(full_stack)
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack.insert(6, 'Python' and 'SQL')
print(full_stack)


# EXERCISE 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age


# Add the min age and the max age again to the list

# Find the median age (one middle item or two middle items divided by two)
median_age = (20 + 25) / 2
print(median_age)

# Find the average age (sum of all items divided by their number )
total = sum(ages) / 10
print(total)

# Find the range of the ages (max minus min)
range_of_the_ages = 26 - 19
print(range_of_the_ages)

# Compare the value of (min - average) and (max - average), use abs() method

# Find the middle country(ies) in the countries list


# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.