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
# The difference is the remove() method require a item exists. And discard no.
it_companies.discard("Facebook")
print(it_companies)
