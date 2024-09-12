#Program: To find the sum of cubes of 'n' natural numbers

def sum_cubes(n):
    cube_sum = (((n * (n+1)) // 2 ) ** 2)
    print(f"The sum of cubes of first {n} natural numbers: {cube_sum}")

n = int(input("Enter the 'n' to calculate sum of cubes of first n natural numbers: "))
sum_cubes(n)
