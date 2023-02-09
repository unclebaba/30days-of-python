# Writ a function which generates a six digit/character random_user_id
import random
import string
def generate_random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for i in range(6))
    return user_id
    print(generate_random_user_id)

# Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is 
# the number of IDs which are supposed to be generated
user_id_gen_by_user = (5, 6)
