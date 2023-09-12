# 1 Create an empty tuple
empty_tuple = ()

# 2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Jose", "Enny", "Giorgio", "Henry", "Elio", "Luiggi")
sisters = ("Maria", "Mafer", "Sara", "Victoria", "Laury")

# 3 Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# 4 How many siblings do you have?
print(len(siblings))

# 5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ("Flor", "Arcadio")
family_members = siblings + parents

# 6 Unpack siblings and parents from family_members
unpack_siblings = family_members[:11]
unpack_parents = family_members[11:]
print(unpack_siblings)
print(unpack_parents)

# 7 Create fruits, vegetables and animal products tuples.
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Mango", "Banana", "Lemon", "Apple")
vegetables = ("Tomato", "Onion", "Potato", "Carrot")
animal_products = ("Milk", "Eggs", "Meat", "Bacon")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 8 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))

# 9 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
i = len(food_stuff_lt) // 2
middle_items = food_stuff_lt[i], food_stuff_lt[i - 1]
print(middle_items)

# 10 Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[9:]
print(first_three)
print(last_three)

# 11 Delete the food_staff_tp tuple completely
del food_stuff_tp

# 12 Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
