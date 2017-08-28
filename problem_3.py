# Problem 3

num = 600851475143

def find_primes(n):
    """
    It finds all the prime numbers up to the integer n.
    """
    assert isinstance(n, int)

    # Uses Sieve of Erasthotenes
    nums = [i for i in range(2, n+1)]
    #print nums
    count = 0
    while count < len(nums):
        current = nums[count]
        to_remove = current**2
        while to_remove <= nums[-1]:
            if to_remove in nums:
                nums.remove(to_remove)
            to_remove += current
        count += 1

    return nums

primes = find_primes(100000)
print primes
