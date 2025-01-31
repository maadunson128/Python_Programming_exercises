def loopfib(n): 
# returns the nth Fibonacci number 
    curr = 1 
    prev = 1 
    for i in range(n-2): 
        curr, prev = curr+prev, curr 
    return curr 



#Recursive fibonacci algo

def recFib(n):
    if n < 3:
        return 1
    else:
        return recFib(n-1) + recFib(n-2)



print(recFib(6))