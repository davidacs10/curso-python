# 1 Declare an empty list
empty_list = []

# 2 Declare a list with more than 5 items
fruit = ["Apple", "Mango", "Lemon", "Orange", "Pineapple"]

# 3 Find the length of your list
print(len(fruit))

# 4 Get the first item, the middle item and the last item of the list
first_item = fruit[0]
middle_item = fruit[2]
last_item = fruit[4]
print(first_item, middle_item, last_item)

# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["David", 25, 1.74, False, "472 Street"]
print(mixed_data_types)

# 6 Declare a list variable named it_companies and assign initial values:
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7 Print the list using print()
print(it_companies)

# 8 Print the number of companies in the list
print(len(it_companies))

# 9 Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[6]
print(first_company, middle_company, last_company)

# 10 Print the list after modifying one of the companies
it_companies[0] = "Sony"
print(it_companies)

# 11 Add an IT company to it_companies
it_companies.append("Samsung")
print(it_companies)

# 12 Insert an IT company in the middle of the companies list
it_companies.insert(4, "Xiaomi")
print(it_companies)

# 13 Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[1].upper())

# 14 Join the it_companies with a string '#;  '
string = "#;  "
it_companies.extend(string)
print(it_companies)

# 15 Check if a certain company exists in the it_companies list.
does_exists = "Motorola" in it_companies
print(does_exists)

# 16 Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17 Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18 Slice out the first 3 companies from the list
print(it_companies[0], it_companies[1], it_companies[2])

# 19 Slice out the last 3 companies from the list
print(it_companies[6], it_companies[7], it_companies[8])

# 20 Slice out the middle IT company or companies from the list
print(it_companies[4])

# 21 Slice out the first 3 companies from the list
it_companies.remove("Xiaomi")
# it_companies.pop(0)
# del it_companies[0]
print(it_companies)

# 22 Remove the middle IT company or companies from the list
it_companies.pop(3)
it_companies.pop(3)
print(it_companies)

# 23 Slice out the last 3 companies from the list
it_companies.remove("Amazon")
# it_companies.pop(4)
# del it_companies[3]
print(it_companies)

# 24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25 Destroy the IT companies list
del it_companies

# 26 Join the following lists:
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
print(front_end.extend(back_end))
