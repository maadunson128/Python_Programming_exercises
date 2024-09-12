x = eval(input("Enter the number between 0 and 1: "))

for i in range(20):
    x = 2 * x * (1 - x)
    print(x)