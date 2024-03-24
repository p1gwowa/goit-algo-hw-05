def caching_fibonacci():                                # Function for caching results
    cache = {}                                          # Dictionary for caching
    def fibonacci(n):                                   # Inner function for calculating fibonacci num
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)      # Fibonacci equation
        print(cache)
        return cache[n]                                 # Inner function return
    return fibonacci                                    # Locking function

fib = caching_fibonacci()                               # Making argument for function

print(fib(-36))
print(fib(1))
print(fib(10))
print(fib(15))
print(fib(16))
print(fib(25))