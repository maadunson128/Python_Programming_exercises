nums = [1, 2, 3, 4, 5, 100]

def recBinary(x, nums, low, high):

    if low > high:
        return -1
    else:
        mid = (low + high) //2

        if x == nums[mid]:
            return mid
        elif x < nums[mid]:
            return recBinary(x, nums, low, mid-1)
        elif x > nums[mid]:
            return recBinary(x, nums, mid+1, high)
        

    
print(recBinary(99, nums, 0, len(nums)-1))