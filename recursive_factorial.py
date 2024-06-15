# Testing factorials!

import time

start_time = time.time()


n = 1000

# Testing recursion
def recursive_factorial(n):
    if (n == 1):
        return 1
    else:
        return recursive_factorial(n-1) * n

print(recursive_factorial(n))

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")


start_time = time.time()
# Testing looping
def loop_factorial(n):
    sum = 0
    for i in range(n):
        sum += n*(n-1)
        n -= 1
    return sum

print(recursive_factorial(n))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")