x1 = eval(input("Enter the number between 0 and 1: "))
x2 = eval(input("Enter the number between 0 and 1 : "))
print("x1 = ",x1, "\t\t", "x2 = ", x2)
print("---------------------------------------")

for i in range(10):
    x1 = 3.9 * x1 * (1 - x1)
    x2 = 3.9 * x2 * (1 - x2)
    print(x1,"\t\t", x2) 