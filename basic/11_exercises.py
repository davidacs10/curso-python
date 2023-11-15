# 1 Python has the module called statistics and we can use this module to do all the statistical calculations.
# However, to learn how to make function and reuse function let us try to develop a program,
# which calculates the measure of central tendency of a sample (mean, median, mode)
# and measure of variability (range, variance, standard deviation).
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample.
# You can create a class called Statistics and create all the functions that do
# statistical calculations as methods for the Statistics class. Check the output below.
import statistics


class Statistics:
    def __init__(self, list):
        self.list = list

    def count(self):
        return f"Count: {len(self.list)}"

    def sum(self):
        total = 0
        for i in self.list:
            total += int(i)
        return f"Sum: {total}"

    def mean(self):
        return f"Mean: {statistics.mean(self.list)}"

    def median(self):
        return f"Median: {statistics.median(self.list)}"

    def mode(self):
        return f"Mode: {statistics.mode(self.list)}"

    def range_statistic(self):
        return f"Range: {max(self.list) - min(self.list)}"

    def variance(self):
        return f"Variance: {statistics.variance(self.list)}"

    def min(self):
        return f"Min: {min(self.list)}"

    def max(self):
        return f"Max: {max(self.list)}"

    def stddev(self):
        return f"Standard deviation: {statistics.stdev(self.list)}"

    def frecuency_distribution(self):
        from collections import Counter

        return dict(Counter(self.list))


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

data = Statistics(ages)
print(data.count())
print(data.sum())
print(data.min())
print(data.max())
print(data.range_statistic())
print(data.mean())
print(data.median())
print(data.mode())
print(data.variance())
print(data.stddev())
print(data.frecuency_distribution())

# 2 Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.


class PersonAccount:
    def __init__(
        self,
        firstname,
        lastname,
    ):
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
        info += f"Incomes: {self.incomes}.\n"
        info += f"Expenses: {self.expenses}.\n"
        info += f"Total incomes: {self.total_incomes()}.\n"
        info += f"Total expenses: {self.total_expenses()}.\n"
        info += f"Account balance: {self.account_balance()}."
        return info


person_account = PersonAccount("David", "Campos")

person_account.add_incomes(1000, "Salary")
person_account.add_incomes(500, "Sales")
person_account.add_expenses(300, "Rent")
person_account.add_expenses(30, "Ethernet")
person_account.add_expenses(100, "Food")
person_account.account_balance()
print(person_account.account_info())
