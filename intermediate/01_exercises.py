# 1 Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_and_zero = [i for i in numbers if i <= 0]
print(negative_and_zero)

# 2 Flatten the following list of lists of lists to a one dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
dimensional_list = [i for sub_list in list_of_lists for inner_list in sub_list for i in inner_list]
print(dimensional_list)

# 3 Using list comprehension create the following list of tuples:
list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)

# 4 Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_list = [[country.upper(), country[:3].upper(), city.upper()] for sub_list in countries for country, city in sub_list]
print(flatten_list)

# 5 Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_dict = [{"country":country.upper(), "city":city.upper()} for sub_list in countries for country, city in sub_list]
print(list_of_dict)

# 6 Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
contatenated_list = [" ".join(i) for sub_list in names for i in sub_list]
print(contatenated_list)