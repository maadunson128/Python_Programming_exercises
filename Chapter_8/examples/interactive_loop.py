##Interactive loop
#Averaging sum

sum:float = 0.0
count:int = 0
isMore = 'yes'
while isMore[0] == 'y':
    sum += float(input("Enter the number: "))
    isMore = input("Do you want to give another number (yes or no): ")
    count += 1


print(f"Average of given numbers: {sum/count}")


