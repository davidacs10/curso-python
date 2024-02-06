### Exercises: Level 1 ###

import re
from collections import Counter

# What is the most frequent word in the following paragraph?

paragraph = """I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities 
to develop an application what else can you love."""

paragraph = paragraph.lower()

pattern = r"\b\w+\b"
words = re.findall(pattern, paragraph, re.I)

word_count = Counter(words)
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_words)

"""The position of some particles on the horizontal x-axis are
 -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8
   in the positive direction. Extract these numbers from this whole 
   text and find the distance between the two furthest particles."""

text = """The position of some particles on the horizontal x-axis are
 -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8
   in the positive direction. Extract these numbers from this whole 
   text and find the distance between the two furthest particles."""

pattern = r"-?\d+"
numbers = re.findall(pattern, text)
numbers = [int(number) for number in numbers]

sorted_points = sorted(numbers)
distance = sorted_points[-1] - sorted_points[0]

print(f"points = {numbers}")
print(f"sorted points = {sorted_points}")
print(f"distance = {distance}")

### Exercises: Level 2 ###

# Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(variable):
    pattern = r"^[a-z][a-z0-9_]*$"
    if re.match(pattern, variable):
        return True
    else:
        return False
    
print(is_valid_variable("firstname10"))

# Clean the following text. After cleaning, count three most frequent words in the string.

sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering 
peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. 
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""

def clean_text(text):
    pattern = r"[%@$&#;]"
    clean = re.sub(pattern, "", text)
    return clean

cleaned_text = clean_text(sentence)
print(clean_text(sentence))

def most_common_words(text):
    words = text.split()
    word_count = Counter(words)

    most_common = word_count.most_common(3)
    return most_common

print(most_common_words(cleaned_text))