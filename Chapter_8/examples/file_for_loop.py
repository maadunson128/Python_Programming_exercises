###Program: Average of numbers using file loops

filename = input("Enter the filename: ")
infile = open(filename, 'r')

total:float = 0.0
count:int = 0
for line in infile:
    x = float(line.strip())
    total += x
    count += 1

print(f"Average of numbers : {total/count}")
