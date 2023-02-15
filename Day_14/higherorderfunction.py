countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Question 1
# Explain the difference between map, filter, and reduce.
"""
The map() function:
The map() function is a type of higher-order. As mentioned earlier, 
this function takes another function as a parameter along with a sequence 
of iterables and returns an output after applying the function to each 
iterable present in the sequence. 
The syntax is as follows: map(function, iterables)  
The filter() function:
The filter() function is used to create an output list consisting of values 
for which the function returns true. 
The syntax is as follows: filter(function, iterables)
The reduce() function:
The reduce() function, as the name describes, applies a given function to the 
iterables and returns a single value.
The syntax is as follows: reduce(function, iterables)
"""

# Question 2
# Explain the difference between higher order function, closure and decorator
""" A decorator really is simply a function that takes another function 
as an argument
while Closure gives access the outer scope of the enclosing function using
a nested function
also
Higher-Order Functions takes a function as an argument or return a function
"""

# Question 3
# Define a call function before map, filter or reduce, see examples.
def funct(m):
    print(str(m))

# Question 4
# Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_list = map(funct,countries)
print(list(countries_list))

# Question 5
# Use for to print each name in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
names_list = map(funct,names)
print(list(names_list))

# Question 6
# Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_list = filter(funct,numbers)
print(list(num_list))

## Exercises: Level 2
# Question 1
# Use map to create a new list by changing each country to 
# uppercase in the countries list
def uppr(m):
    return str(m).upper()
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_list = map(uppr,countries)
print(list(countries_list))

# Question 2
# Use map to create a new list by changing each number to its square
# in the numbers list
def square(x):
    return x*x
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_list = map(square,numbers)
print(list(num_list))

# Question 3
# Use map to change each name to uppercase in the names list

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
names_list = map(uppr,names)
print(list(names_list))

# Question 4
# Use filter to filter out countries containing 'land
def ends_with_land(m):
    if m[-4:] == 'land':
        print(m)
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_list = filter(ends_with_land,countries)
print(list(countries_list))

# Question 5
# Use filter to filter out countries having exactly six characters.
def len_equalto_six(m):
    if len(m) == 6:
        return m
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_list = filter(len_equalto_six,countries)
print(list(countries_list))

# Question 6
# Use filter to filter out countries containing six letters and 
# more in the country list.
def len_morethan_five(m):
    if len(m) >= 6:
        return m
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_list = filter(len_morethan_five,countries)
print(list(countries_list))

# Question 7
# Use filter to filter out countries starting with an 'E'
def start_with_land(m):
    if m[0] == 'E':
        return m
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_list = filter(start_with_land,countries)
print(list(countries_list))

# Question 8
# Chain two or more list iterators 
# (eg. arr.map(callback).filter(callback).reduce(callback))


# Question 10
# Use reduce to sum all the numbers in the numbers list.
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_numbers(x,y):  
    return x + y    
total = reduce(sum_numbers,numbers)
print(total)

# Question 11
# Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_message(x,y):
    return f'{x}, {y}' + 'is a north European countries'

total = reduce(get_message,countries)
print(total)

# Question 12
# Declare a function called categorize_countries that returns a list 
# of countries with some common pattern (you can find the countries list 
# in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
def categorize_countries():
    return 0

# Question 14
# Declare a get_first_ten_countries function - it returns a list of first 
# ten countries from the countries.js list in the data folder.
def get_first_ten_countries(fcountires):
    return fcountires
first_10_countries = map(get_first_ten_countries,countries)
print(list(first_10_countries)[:10])

# Question 15
# Declare a get_last_ten_countries function that returns 
# the last ten countries in the countries list
def get_last_ten_countries(x):
    return x
mm = map(get_last_ten_countries,countries)
print(list(mm)[-10:])