# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word_1 = "Thirty"
word_2 = "Days"
word_3 = "Of"
word_4 = "Python"
space = " "
first_string = word_1 + space + word_2 + space + word_3 + space + word_4
print(first_string)

# 2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
word_1 = "Coding"
word_2 = "For"
word_3 = "All"
second_string = word_1 + space + word_2 + space + word_3
print(second_string)

# 3 Declare a variable named company and assign it to an initial value "Coding For All".
company = second_string

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
# company = second_string[7:]
# print(company)

# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
sub_string = "Coding"
print(company.index(sub_string))
print(company.find("Coding"))

# 11 Replace the word coding in the string 'Coding For All' to Python.
print(f"{word_4} {word_2} {word_3}")

# 12 Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace("Coding For All", "Python For Everyone"))

# 13 Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook Google Microsoft Apple IBM Oracle Amazon".split())

# 15 What is the character at index 0 in the string Coding For All.
print(company[0])

# 16 What is the last index of the string Coding For All.
print(company[-1])

# 17 What character is at index 10 in "Coding For All" string.
print(company[10])

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
abbr_1 = "PFE"

# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
abbr_2 = "CFA"

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
print(company.find("C"))

# 21 Use index to determine the position of the first occurrence of F in Coding For All.
print(company.find("F"))

# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
company = "Coding For All People"
print(company.rfind("l"))

# 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))

# 24 Use rindex to find the position of the last occurrence of the word because in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.rfind("because"))

# 25 Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])

# 26 Find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"))

# 27 Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])

# 28 Does ''Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

# 29 Does 'Coding For All' end with a substring coding?
print("Coding For All".endswith("All"))

# 30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print("   Coding For All      ".strip("     "))

# 31 Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython = False
# thirty_days_of_python = True
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 32 The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
result = "# ".join(libraries)
print(result)

# 33 Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34 Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\t\tCity\nDavid\t26\tVenezuela\tAnzoategui")

# 35 Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius**2
format_string = "The area of a circle with radius {} is {} meters square.".format(
    radius, area
)
print(format_string)

# 36 Make the following using string formatting methods:
a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} ** {} = {}".format(a, b, a**b))
print("{} // {} = {}".format(a, b, a // b))
