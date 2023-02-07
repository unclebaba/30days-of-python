# Create an empty tuple
empty_tuple = tuple()
print(empty_tuple)

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("ola", "femi")
sisters = ("hassana", "maryam")

# Join brothers and sisters tuples and assign it to siblings
siblings = (brothers) + (sisters)
print(siblings)

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = ('baba', 'lami') + tuple(siblings)
print(family_members)





# Exercises: Level 
# Unpack siblings and parents from family_members


# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = 'banana', 'orange', 'mango', 'lemon'
vegetables = 'carrot', 'spinach', 'bitterleaf'
animal_products = 'egg', 'fat', 'milk', 'cheese'
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
print(list(food_stuff_tp))

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
spinach = food_stuff_tp[-6]
print(spinach)

# Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_tp[3:]
print(first_three_items)
last_three_items = food_stuff_tp[:8]
print(last_three_items)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
food_staff_tp = ('banana', 'orange', 'mango', 'lemon', 'carrot', 'spinach', 'bitterleaf', 'egg', 'fat', 'milk', 'cheese')
print('spinach' in food_staff_tp)

# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries )

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries )

