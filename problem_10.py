# Problem 10

import math

def find_primes(n):
    """
    It finds all the prime numbers up to the integer n.
    """
    assert isinstance(n, int)

    # Uses Sieve of Erasthotenes
    nums = [True for i in range(n)]
    for i in range(int(n**(0.5))):
        if i == 0 or i == 1:
            nums[i] = False
        else:
            for k in range(int(math.ceil(float(n)/i - i))):
                nums[i**2+k*i] = False
    primes = []
    for i in range(n):
        if nums[i]:
            primes.append(i)
    return primes

primes = find_primes(20000)
total_sum = 0
for i in primes:
    total_sum += i

print total_sum
