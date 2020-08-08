import time
import functools

fibonacci_cache = {}

def memoize(function):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            val = function(*args)
            cache[args] = val
            return val
    return decorated_function

def fibonacci(n: int):
    if(n <= 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_with_memoization(n: int):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if(n <= 0):
        value = 0
    elif(n == 1):
        value = 1
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_cache[n] = value
    print(fibonacci_cache)
    return value

@memoize
def fib_decorator(n):
    if n < 2:
        return n
    else:
        return fib_decorator(n-1) + fib_decorator(n-2)

@functools.lru_cache(maxsize=None) #128 by default
def fib_func(num):
    if num < 2:
        return num
    else:
        return fib_func(num-1) + fib_func(num-2)

if __name__ == "__main__":

    start_time = time.perf_counter()
    print(fibonacci(30))
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Finished in {run_time:.4f} secs")

    start_time = time.perf_counter()
    print(fibonacci_with_memoization(30))
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Finished in {run_time:.4f} secs")

    start_time = time.perf_counter()
    print(fib_decorator(300))
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Finished in {run_time:.4f} secs")

    start_time = time.perf_counter()
    print(fib_func(300))
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Finished in {run_time:.4f} secs")
    