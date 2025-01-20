###Program: statSet

import math

class StatSet:
    def __init__(self):
        """Initializes a StatSet with no data."""
        self.data = []

    def addNumber(self, x):
        """Adds a number x to the dataset."""
        self.data.append(x)

    def mean(self):
        """Returns the mean of the numbers in the dataset."""
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)

    def median(self):
        """Returns the median of the numbers in the dataset."""
        if not self.data:
            return 0
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def stdDev(self):
        """Returns the standard deviation of the numbers in the dataset."""
        if not self.data:
            return 0
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return math.sqrt(variance)

    def count(self):
        """Returns the count of numbers in the dataset."""
        return len(self.data)

    def min(self):
        """Returns the smallest value in the dataset."""
        if not self.data:
            return None
        return min(self.data)

    def max(self):
        """Returns the largest value in the dataset."""
        if not self.data:
            return None
        return max(self.data)



def main():
    # Create a StatSet object
    stats = StatSet()

    # Add numbers to the dataset
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for num in numbers:
        stats.addNumber(num)

    # Print statistics
    print("Dataset:", numbers)
    print("Mean:", stats.mean())
    print("Median:", stats.median())
    print("Standard Deviation:", stats.stdDev())
    print("Count:", stats.count())
    print("Minimum:", stats.min())
    print("Maximum:", stats.max())


if __name__ == "__main__":
    main()