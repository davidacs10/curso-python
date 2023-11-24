it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1 Find the length of the set it_companies
print(len(it_companies))
# 2 Add 'Twitter' to it_companies
it_companies.add("Twitter")
# 3 Insert multiple IT companies at once to the set it_companies
it_companies.update(["Samsung", "YouTube", "OpenIA"])
print(it_companies)
# 4 Remove one of the companies from the set it_companies
it_companies.remove("Facebook")
print(it_companies)
# 5 What is the difference between remove and discard
# La diferencia es que discard no genera error en caso de no encontrarse el item. Remove si genera un error en caso de que no este.
it_companies.discard("Hola")
print(it_companies)
# 6 Join A and B
a_b = A.union(B)
print(a_b)
# 7 Find A intersection B
print(A.intersection(B))
# 8 Is A subset of B
print(A.issubset(B))
print(B.issuperset(A))
# 9 Are A and B disjoint sets
print(B.isdisjoint(B))
# 10 Join A with B and B with A
A.union(B)
print(A.union(B))
B.union(A)
print(B.union(A))
# 11 What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# 12 Delete the sets completely
del A
del B
# 13 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(len(age))
age = set(age)
print(len(age))
# 14 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
text = "I am a teacher and I love to inspire and teach people"
word = text.split()
unique_words = set(word)
print(len(unique_words))
print(unique_words)
