###Statistics - Mean, median, standard deviation
from math import sqrt
def getNums()->list[int]:
    x = input("Enter a number: ")
    nums:list[int] = []

    while x != "":
        nums.append(float(x))
        x = input("Enter a number: ")

    return nums

def getMean(nums:list[int])->float:
    num:int = 0
    for x in nums:
        num += x

    return num/len(nums)


def getMedian(nums:list[int])->int:
    nums.sort()
    med:int = None
    size:int = len(nums)
    mid:int = size //2

    if mid % 2 == 0:
        med = nums[mid] + nums[mid-1]
    else:
        med = nums[mid]

    return med

def getSd(mean:float, nums:list[int])->float:
    sumsq:int = 0
    for x in nums:
        sumsq += (mean - x)**2

    return sqrt(sumsq/len(nums)-1)
    


def main()->None:

    #getting numbers
    nums = getNums()

    #calculating the statistics terms
    mean = getMean(nums)
    median = getMedian(nums)
    sd = getSd(mean, nums)

    print(f"Mean: {mean} \nMedian: {median} \nStandard Deviation: {sd}")

main()