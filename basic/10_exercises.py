# 1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers(2, 3))


# 2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    PI = 3.14
    area = PI * r**2
    return area


print(area_of_circle(10))


# 3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
        else:
            return "Please only add numbers"

    return total


print(add_all_nums(1, 3, 5))


# 4 Temperature in °C can be converted to °F using this formula:
# °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f


print(convert_celsius_to_fahrenheit(40.5555556))


# 5 Write a function called check-season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    season_mapping = {
        "january": "Winter",
        "february": "Winter",
        "march": "Spring",
        "april": "Spring",
        "may": "Spring",
        "june": "Summer",
        "july": "Summer",
        "august": "Summer",
        "september": "Autumn",
        "october": "Autumn",
        "november": "Autumn",
        "december": "Winter",
    }
    if month in season_mapping:
        return season_mapping[month]
    else:
        return "Invalid Month"


print(check_season("december"))
