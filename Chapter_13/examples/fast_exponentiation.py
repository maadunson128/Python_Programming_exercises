####Program: Exponentiation (finding value of a power n)


def recPow(a, n):
    if n == 0:
        return 1
    else:
        factor = recPow(a, n//2)

        if n % 2 ==0:
            return factor * factor 
        else:
            return factor * factor * a
        

print(recPow(10, 3))