# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
for j in range(11):
    print(j)
# using while loop.
    j = 0
while j < 11:
    print(j)
    j += 1

# Iterate 10 to 0 using for loop, do the same using while loop.
for j in range(10, -1, 1):
    print(j)
# using while loop.
j = 10
while j >= 0:
    print(j)
    j -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  ########
for j in range(1, 8):
    print('#' * j)

# Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for j in range(8):
    for j in range(16):
        if j % 2 == 0:
            print('#', end=' ')
        else:
            print(' ', end=' ')
    print('')

# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for j in range(11):
    print(f"{j} x {j} = {j*j}")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.
prog_lang = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in prog_lang:
    print(item)

# Use for loop to iterate from 0 to 100 and print only even numbers
for j in range(101):
    if j % 2 == 0:
        print(j)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for j in range(101):
    if j % 2 != 0:
        print(j)


        # Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum = 0
for j in range(101):
    sum += j
print("The sum of all numbers from 0 to 100 is:", sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even_num = 0
for j in range(101):
    if j % 2 == 0:
      sum_even_num += j
print("The sum of all even numbers from 0 to 100 is:", sum_even_num)
