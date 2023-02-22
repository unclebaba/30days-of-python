## The position of some particles on the horizontal x-axis are 
# -12, -4, -3 and -1 in the negative direction, 0 at origin, 
# 4 and 8 in the positive direction. Extract these numbers 
# from this whole text and find the distance between the two 
# particles.
import re
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
pattern = r"-?\d+"
matches = re.findall(pattern, text)
points = [int(match) for match in matches]

furthest_points = min(points), max(points)
distance = abs(furthest_points[1] - furthest_points[0])
print(distance)





## Write a pattern which identifies if a string is a valid python variable

# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True
import re
def is_valid_variable(variable_name):
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    return bool(pattern.match(variable_name))
print(is_valid_variable('first_name')) 
print(is_valid_variable('first-name')) 
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))  

## Clean the following text. After cleaning, count three most frequent 
# words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# print(clean_text(sentence));
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
import re
from collections import Counter

def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text
def most_frequent_words(text):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(3)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))