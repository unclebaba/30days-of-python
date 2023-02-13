# Writ a function which generates a six digit/character random_user_id
import random
import string
def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for i in range(6))
    return user_id


# Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is 
# the number of IDs which are supposed to be generated
def user_id_gen_by_user():
    length = int(input("number of characters for the ID: "))
    count = int(input("number of IDs to generate: "))
    chars = string.ascii_letters + string.digits
    user_ids = []
    for i in range(count):
        user_ids.append(''.join(random.choices(chars, k=length)))
    return user_ids

print(user_id_gen_by_user())
print(user_id_gen_by_user())




def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return "rgb({}, {}, {})".format(red, green, blue)
print(rgb_color_gen())





def list_of_hexa_colors(n):
    hexa_colors = []
    for i in range(n):
        color = "#"
        for j in range(6):
            color += random.choice(string.hexdigits)
        hexa_colors.append(color)
    return hexa_colors
print(list_of_hexa_colors(5))





def list_of_rgb_colors(num):
    rgb_colors = []
    for i in range(num):
        red = str(random.randint(0, 255))
        green = str(random.randint(0, 255))
        blue = str(random.randint(0, 255))
        rgb_colors.append("rgb(" + red + "," + green + "," + blue + ")")
    return rgb_colors
print(list_of_rgb_colors(5))




def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return [''.join([random.choice('0123456789abcdef') for j in range(6)]) for i in range(num_colors)]
    elif color_type == 'rgb':
        return ['rgb({}, {}, {})'.format(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for i in range(num_colors)]
    else:
        return None
print(generate_colors(5, 7))



def generate_colors(color_type, num):
    colors = []
    if color_type == 'hexa':
        for i in range(num):
            color = "#"
            for j in range(6):
                color += random.choice("0123456789abcdef")
            colors.append(color)
    elif color_type == 'rgb':
        for i in range(num):
            color = "rgb("
            for j in range(3):
                color += str(random.randint(0, 255))
                if j < 2:
                    color += ","
            color += ")"
            colors.append(color)
    return colors
print(generate_colors('hexa', 3)) 
print(generate_colors('hexa', 1)) 
print(generate_colors('rgb', 3))  
print(generate_colors('rgb', 1))  



def shuffle_list(lst):
    random.shuffle(lst)
    return lst


def unique_random_numbers():
    random_numbers = random.sample(range(10), 7)
    return random_numbers

print(unique_random_numbers())