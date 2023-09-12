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
front_end.extend(back_end)
print(front_end)

# 27 After joining the lists in question 26.
# Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = ["Python", "SQL", "Redux"]
front_end.extend(full_stack)
print(front_end)

# 28 The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print(ages)
# Add the min age and the max age again to the list
ages.append(19)
ages.append(26)
print(ages)
# Find the median age (one middle item or two middle items divided by two)
print(ages.index(24))
# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print(average_age)
# Find the range of the ages (max minus min)
min_list = min(ages)
max_list = max(ages)
print(min_list, max_list)
# Compare the value of (min - average) and (max - average), use abs() method
min_average = abs(min_list - average_age)
max_average = abs(max_list - average_age)
compare_value = min_average > max_average
print(min_average, max_average)
print(compare_value)

# 29 Find the middle country(ies) in the countries list
countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cape Verde",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombi",
    "Comoros",
    "Congo (Brazzaville)",
    "Congo",
    "Costa Rica",
    "Cote d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor Timur)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia, The",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macedonia",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia and Montenegro",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Swaziland",
    "Sweden",
    "Switzerland",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]
n = len(countries)
i = n // 2
half = countries[i]
print(half)
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[: i + 1]
second_half = countries[i + 1 :]
print(first_half)
print(second_half)
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
# Unpack the first three countries and the rest as scandic countries.
countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
first_country, second_country, third_country, *scandic = countries
print(first_country)
print(second_country)
print(third_country)
print(scandic)
