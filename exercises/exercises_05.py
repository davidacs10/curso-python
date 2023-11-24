# 1 Declare an empty list
empty_list = []
# 2 Declare a list with more than 5 items
tech_languages = ["Go", "Python", "JavaScript", "TypeScript", "Rust"]
# 3 Find the length of your list
print(len(tech_languages))
# 4 Get the first item, the middle item and the last item of the list
first_item = tech_languages[0]
middle_item = tech_languages[len(tech_languages) // 2]
last_item = tech_languages[4]
print(f"first item: {first_item}, middle_item: {middle_item}, last_item: {last_item}")
# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["David", 25, 1.80, False, [6050, "Street 400"]]
print(mixed_data_types)
# 6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# 7 Print the list using print()
print(it_companies)
# 8 Print the number of companies in the list
print(len(it_companies))
# 9 Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[6]
print(
    f"first_company: {first_company}, middle_compnay: {middle_company}, last_company: {last_company}"
)
# 10 Print the list after modifying one of the companies
it_companies[4] = "Samsung"
print(it_companies)
# 11 Add an IT company to it_companies
it_companies.append("OpenIA")
print(it_companies)
# 12 Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "Sony")
print(it_companies)
# 13 Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())
# 14 Join the it_companies with a string '#;  '
my_string = "#;  "
my_new_list = my_string.join(it_companies)
print(my_new_list)
# 15 Check if a certain company exists in the it_companies list.
print(it_companies.index("Amazon"))
# 16 Sort the list using sort() method
it_companies.sort()
print(it_companies)
# 17 Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
# 18 Slice out the first 3 companies from the list
slice_first = it_companies[:3]
print(slice_first)
# 19 Slice out the last 3 companies from the list
slice_last = it_companies[6:]
print(slice_last)
# 20 Slice out the middle IT company or companies from the list
slice_middle = it_companies[len(it_companies) // 2]
print(slice_middle)
# 21 Remove the first IT company from the list
print(it_companies.pop(0))
# 22 Remove the middle IT company or companies from the list
del it_companies[len(it_companies) // 2]
print(it_companies)
# 23 Remove the last IT company from the list
print(it_companies.pop(-1))
# 24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# 25 Destroy the IT companies list
del it_companies
# 26 Join the following lists:
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
front_end.extend(back_end)
print(front_end)
# 27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)
# 28 The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# 29 Sort the list and find the min and max age
ages.sort()
print(ages)
print(f"Min age: {min(ages)}")
print(f"Max age: {max(ages)}")
# 30 Add the min age and the max age again to the list
ages.append(min(ages))
ages.append(max(ages))
print(ages)
# 31 Find the median age (one middle item or two middle items divided by two)
sorted_ages = sorted(ages)
length = len(sorted_ages)
middle = length // 2
median = (sorted_ages[middle - 1] + sorted_ages[middle]) / 2
print(median)
print((sorted_ages[len(sorted_ages) // 2 - 1] + sorted_ages[len(sorted_ages) // 2]) / 2)
# 32 Find the average age (sum of all items divided by their number )
average = sum(sorted_ages) / length
print(average)
# 33 Find the range of the ages (max minus min)
range_ages = max(sorted_ages) - min(sorted_ages)
print(range_ages)
# 34 Compare the value of (min - average) and (max - average), use abs() method
print(abs(min(sorted_ages) - average))
print(abs(max(sorted_ages) - average))
# 35 Find the middle country(ies) in the countries list
from data import country

countries = country.countries

middle_countries = countries
print(middle_countries)
print(middle_countries[len(middle_countries) // 2 - 1])
print(middle_countries[len(middle_countries) // 2])
# 36 Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[: len(countries) // 2 + 1]
second_half = countries[len(countries) // 2 + 1 :]
print(first_half)
print(second_half)
print(len(first_half))
print(len(second_half))
# 37 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
new_list = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
china, russia, usa, *scandic = new_list
print(china)
print(russia)
print(usa)
print(scandic)
