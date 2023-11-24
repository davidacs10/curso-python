# Tuplas

# 1 Create an empty tuple
my_tuple = ()
print(type(my_tuple))
# 2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("David", "Jose")
sisters = ("Angelica", "Victoria")
# 3 Join brothers and sisters tuples and assign it to siblings
sibling = brothers + sisters
# 4 How many siblings do you have?
print(len(sibling))
# 5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ("Arcadio", "Flor")
family_members = parents + sibling
print(family_members)
# 6 Unpack siblings and parents from family_members
sibling = family_members[2:]
parents = family_members[:2]
print(sibling)
print(parents)
# 7 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Mango", "Lemon", "Orange")
vegetables = ("Potato", "Onion", "Tomato")
animal_products = ("Milk", "Meat", "Butter")
food_stuff_tp = fruits + vegetables + animal_products
# 8 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
# 9 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items = len(food_stuff_tp) // 2
print(food_stuff_tp[middle_items])
# 10 Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_tp[0:3]
last_three = food_stuff_tp[6:]
print(f"first three: {first_three}. last three: {last_three}.")
# 11 Delete the food_staff_tp tuple completely
del food_stuff_tp
# 12 Check if an item exists in tuple:
print("Lemon" in fruits)
# 13 Check if 'Estonia' is a nordic country
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
is_estonia_nordic = "Estonia" in nordic_countries
print(is_estonia_nordic)
# 14 Check if 'Iceland' is a nordic country
is_iceland_nordic = "Iceland" in nordic_countries
print(is_iceland_nordic)
