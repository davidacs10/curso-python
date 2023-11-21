# Strings

# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string_1 = "Thirty"
string_2 = "Days"
string_3 = "Of"
string_4 = "Python"
print(f"{string_1} {string_2} {string_3} {string_4}")
# 2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_1 = "Coding"
string_2 = "For"
string_3 = "All"
print(f"{string_1} {string_2} {string_3}")
# 3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
# 4 Print the variable company using print().
print(company)
# 5 Print the length of the company string using len() method and print().
print(len(company))
# 6 Change all the characters to uppercase letters using upper() method.
print(company.upper())
# 7 Change all the characters to lowercase letters using lower() method.
print(company.lower())
# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# 9 Cut(slice) out the first word of Coding For All string.
company = company[1:]
print(company)
# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
company = "Coding For All"
string_1 = "Coding"
print(company.index(string_1))
print(company.find(string_1))
# 11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace(string_1, string_4))
# 12 Change Python for Everyone to Python for All using the replace method or other methods.
string_5 = "Everyone"
company = f"{string_4} {string_2} {string_5}"
print(company)
print(company.replace(string_5, string_3))
# 13 Split the string 'Coding For All' using space as the separator (split()) .
company = "Coding For All"
subcadena = company.split(" ")
print(company.split(" "))
print(subcadena)
# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(" ")
print(split_companies)
# 15 What is the character at index 0 in the string Coding For All.
company = company[0]
print(company)
# 16 What is the last index of the string Coding For All.
company = "Coding For All"
company = company[-1]
print(company)
# 17 What character is at index 10 in "Coding For All" string.
company = "Coding For All"
company = company[10]
print(company)
# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym_1 = "Python For Everyone"
poovo = acronym_1[::4]
print(poovo)
# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
acronym_2 = "Coding For All"
cnol = acronym_2[::4]
print(cnol)
# 20 Use index to determine the position of the first occurrence of C in Coding For All.
cfa = "Coding For All"
sub_string = cfa.index("C")
print(sub_string)
# 21 Use index to determine the position of the first occurrence of F in Coding For All.
cfa = "Coding For All"
sub_string = cfa.index("F")
print(sub_string)
# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
cfap = "Coding For All People"
sub_string = cfap.rfind("l")
print(sub_string)
# 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
occurrence = "You cannot end a sentence with because because because is a conjunction"
print(occurrence.index("because"))
print(occurrence.find("because"))
# 24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
occurrence = "You cannot end a sentence with because because because is a conjunction"
print(occurrence.rindex("because"))
# 25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
occurrence = "You cannot end a sentence with because because because is a conjunction"
print(occurrence.rfind("e"))
print(occurrence[31:54])
# 26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sub_string = "because"
print(occurrence.find(sub_string))
# 27 Does ''Coding For All' start with a substring Coding?
string_101 = "Coding For All"
sub_string = "Coding"
print(string_101.startswith(sub_string))
# 28 Does 'Coding For All' end with a substring coding?
print(string_101.endswith(sub_string))
# 29 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string_101 = "   Coding For All    "
print(string_101.strip())
