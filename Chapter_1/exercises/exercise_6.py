x = eval(input("Enter a number between 0 to 1: "))

for i in range(100):
    x = 3.9 * x * (1-x)
    print(x)

print("-----------------------------------------------")
for i in range(100):
    x = 3.9 * (x - x * x)
    print(x)

print("-----------------------------------------------")

for i in range(100):
    x = 3.9 * x - 3.9 * x * x
    print(x)
