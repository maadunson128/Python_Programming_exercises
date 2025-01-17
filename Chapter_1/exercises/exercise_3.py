x = eval(input("Enter a number between 0 to 1: "))

for i in range(10):
    x = 2 * x * (1 - x)
    print(x,end="\n")


"""From the previous example : 
    - The function iterates 10 times and gives different value for each iteration.
    if we change the input value, the last value will change significantly.

"""

'''From this exercise, we can see that if we give any value, it will give some value and final value will be aprroximate to .5'''