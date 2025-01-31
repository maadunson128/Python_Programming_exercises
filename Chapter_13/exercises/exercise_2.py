###Program: Fibonacci counter

class Fibonacci:
    def __init__(self):
        self.counter = 0

    def recFib(self,n):
        self.counter += 1
        if n < 3:
            return 1
        else:
            return self.recFib(n-1) + self.recFib(n-2)
        
    def getCount(self):
        return self.counter
    


fib = Fibonacci()
print(fib.recFib(23))

print(f"No of time fib() called: {fib.getCount()}")