# # 1 Iterate 0 to 10 using for loop, do the same using while loop.
# for number in range(11):
#     print(number)

# count = 0
# while count < 11:
#     print(count)
#     count = count + 1

# # 2 Iterate 10 to 0 using for loop, do the same using while loop.
# for number in range(10, -1, -1):
#     print(number)

# count = 10
# while count >= 0:
#     print(count)
#     count = count - 1

# 3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# for i in range(1, 8):
#     print("#" * i)

# 4 Use nested loops to create the following:
# for _ in range(8):
#     for _ in range(8):
#         print("#", end=" ")
#     print()

# # 5 Print the following pattern:
# for i in range(11):
#     for _ in range(11):
#         result = _ * i
#         if _ != i:
#             continue
#         print(f"{_} x {i} =", result)

# for i in range(11):  # Iteramos desde 0 hasta 10
#     result = i * i  # Calculamos el resultado de la multiplicación
#     print(f"{i} x {i} = {result}")

# 6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# stack = ["Python", "Numpy", "Pandas", "Django", "Flask"]
# for _ in stack:
#     print(_)

# 7 Use for loop to iterate from 0 to 100 and print only even numbers
# for number in range(2, 102, 2):
#     print(number)

# 8 Use for loop to iterate from 0 to 100 and print only odd numbers
# for number in range(0, 100):
#     if number % 2 == 0:
#         continue
#     print(number)

# 9 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
number = 0
for i in range(101):
    print(number + i)
