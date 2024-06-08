x = eval(input("Enter the number between 0 and 1: "))
n = eval(input("How many times I want to print the x ?"))

for i in range(n):
    x = 2 * x * (1-x)
    print(x)