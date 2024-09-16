###Program: Squaring elements in a  list

#function to square a number
def square(num:float)->float:
    return num **2

#function to square each element in a list
def squareEach(nums)->None:

    #squaring each element in the list
    for i, num in enumerate(nums):
        nums[i] = square(num)


def main()->None:

    #input from the user : list of numbers
    nums:list[float] = [1.0, 2.0, 3.0, 4.0, 5.0]

    #Squaring each num in the list
    squareEach(nums)

    print(f'List after squaring each element : {nums}')

main()
