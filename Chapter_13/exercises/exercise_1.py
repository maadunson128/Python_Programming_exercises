###Program: Counting the compution of fibonacci in recursion
def recFib(n):
    print(f"Computing fib({n})")
    if n < 3:
        print(f"Leaving fib({n}) returning 1")
        return 1
    else:
        ans = recFib(n-1) + recFib(n-2)
        print(f"Leaving fib({n}) returning {ans}")
        return ans
    
    



print(recFib(6))