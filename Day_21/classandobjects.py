## Python has the module called statistics and we can use this module to do all the statistical calculations. 
# However, to learn how to make function and reuse function let us try to develop a program, 
# which calculates the measure of central tendency of a sample (mean, median, mode) 
# and measure of variability (range, variance, standard deviation). In addition to those measures, 
# find the min, max, count, percentile, and frequency distribution of the sample. 
# You can create a class called Statistics and create all the functions that do statistical 
# calculations as methods for the Statistics class. Check the output below.

class Statistics:
    def _init_(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2-1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]
    def mode(self):
        frequencies = {}
        for x in self.data:
            if x in frequencies:
                frequencies[x] += 1
            else:
                frequencies[x] = 1
        mode = None
        max_count = 0
        for value, count in frequencies.items():
            if count > max_count:
                mode = value
                max_count = count
        return {"mode": mode, "count": max_count}

    def std(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / (len(self.data) - 1)
        return variance ** 0.5

    def var(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / (len(self.data) - 1)

    def percentile(self, p):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        k = (n - 1) * p
        f = int(k)
        c = k - f
        if f + 1 < n:
            return sorted_data[f] + c * (sorted_data[f+1] - sorted_data[f])
        else:
            return sorted_data[f]

    def freq_dist(self):
        frequencies = {}
        for x in self.data:
            if x in frequencies:
                frequencies[x] += 1
            else:
                frequencies[x] = 1
        return frequencies

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:', data.count()) 
print('Sum: ', data.sum()) 
print('Min: ', data.min()) 
print('Max: ', data.max()) 
print('Range: ', data.range()) 
print('Mean: ', data.mean()) 
print('Median: ', data.median()) 
print('Mode: ', data.mode()) 
print('Standard Deviation: ', data.std()) 
print('Variance: ', data.var()) 
print('25th Percentile: ', data.percentile(0.25))


## Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties 
# and it has total_income, total_expense, account_info, add_income, add_expense and 
# account_balance methods. Incomes is a set of incomes and its description. 
# The same goes for expenses.
class PersonAccount:
    def _init_(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        return f"{self.firstname} {self.lastname}'s account balance: {self.account_balance()}"

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def account_balance(self):
        return self.total_income() - self.total_expense()
