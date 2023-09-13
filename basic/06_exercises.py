# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1 Find the length of the set it_companies
print(len(it_companies))

# 2 Add 'Twitter' to it_companies
it_companies.update(["Twitter"])
print(it_companies)

# 3 Insert multiple IT companies at once to the set it_companies
other_companies = ["Oracle", "Telegram", "Samsung"]
it_companies.update(other_companies)
print(it_companies)

# 4 Remove one of the companies from the set it_companies
it_companies.remove("Facebook")
print(it_companies)

# 5 What is the difference between remove and discard
# The difference is the remove() method require a item exists. And discard doesn't require it.
it_companies.discard("Facebook")
print(it_companies)

# 6 Join A and B
print(A.union(B))

# 7 Find A intersection B
print(A.intersection(B))

# 8 Is A subset of B
print(A.issubset(B))  # True

# 9 Are A and B disjoint sets
print(A.isdisjoint(B))

# 10 Join A with B and B with A
A.update(B)
print(A)
print(B.union(A))

# 11 What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

result = A.symmetric_difference(B)
print(result)

# 12 Delete the sets completely
del A
del B

# 13 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(len(age))
ageset = set(age)
print(len(ageset))
print(len(age) > len(ageset))

# 14 Explain the difference between the following data types: string, list, tuple and set.
# string: es una cadena de texto
# list: es una cadena de elementos organizada, mutable y se pueden repetir los elementos
# tuple: es una cadena de elementos organizada, no mutables y se pueden repetir los elementos
# set: es una cadena de elementos no organizada, no mutables. Pero se pueden agregar nuevos elementos. No repetidos.

# 15 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?
# Use the split methods and set to get the unique words.
teach = "I am a teacher and I love to inspire and teach people"
words = teach.split()
unique_words = len(set(words))
print(unique_words)
