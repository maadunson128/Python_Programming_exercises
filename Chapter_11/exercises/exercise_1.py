###Program: Mean and standard deviation

from math import sqrt

class Library:
    def __init__(self):
        '''Nothing'''
        pass

    def mean(self, nums):
        '''Finds the mean'''
        self.mean =  sum(nums) / len(nums)
        return self.mean

    def stdDev(self, nums):
        '''Finds the standard deviation'''
        sumsq:int = 0
        for x in nums:
            sumsq += (self.mean - x)**2

        self.std = sqrt(sumsq/len(nums)-1)
        return self.std

    def meanStdDev(self, nums):
        return self.mean, self.std
        


def main()->None:
    #creating nums -> list of numbers
    nums = [1, 5, 7, 20, -10]

    #using the library methods
    lib = Library()

    print(f"Mean: {lib.mean(nums)}\nStandard deviation: {lib.stdDev(nums)}")

    #printing both mean and standard deviation
    mean, stdDev = lib.meanStdDev(nums)
    print(f"Mean and std deviation: {mean}, {stdDev}")
    

main()