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
        return f"Frequency Distribution: {statistics.frq}"


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
