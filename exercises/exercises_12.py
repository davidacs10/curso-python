import statistics
from collections import Counter

# 1 Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

ages = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]


class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return self.data

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def mean(self):
        return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)

    def mode(self):
        mode_result = Counter(self.data).most_common(1)
        return {"mode": mode_result[0][0], "count": mode_result[0][1]}

    def stdev(self):
        return statistics.stdev(self.data)

    def variance(self):
        return statistics.variance(self.data)

    def freq_dist(self):
        counter = Counter(self.data)
        return [(count, value) for value, count in counter.items()]


data = Statistics(ages)
print(data.count())
print(data.sum())
print(data.min())
print(data.max())
print(data.range())
print(data.mean())
print(data.median())
print(data.mode())
print(data.stdev())
print(data.variance())
print(data.freq_dist())


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_incomes(self, amount, description):
        self.incomes[description] = amount

    def add_expenses(self, amount, description):
        self.expenses[description] = amount

    def total_incomes(self):
        return sum(self.incomes.values())

    def total_expenses(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_incomes() - self.total_expenses()

    def account_info(self):
        info = f"{self.firstname} {self.lastname}.\n"
        info += f"Incomes: {self.incomes}\n"
        info += f"Expenses: {self.expenses}\n"
        info += f"Total incomes: {self.total_incomes()}\n"
        info += f"Total expenses: {self.total_expenses()}\n"
        info += f"Account balance: {self.account_balance()}\n"
        return info


person1 = PersonAccount("David", "Campos")
person1.add_incomes(1000, "Salary")
person1.add_incomes(500, "Sales")
person1.add_incomes(500, "Freelance")
person1.add_expenses(200, "Rent")
person1.add_expenses(50, "Ethernet")
person1.add_expenses(200, "Food")
print(person1.account_info())
