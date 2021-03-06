# Problem 12

def check_divisors(n):
    """ Returns the amount of divisors for integer n. """
    assert isinstance(n, int)

    count = 1
    for i in range(1,int(n**(0.5))+1):
        if n%i == 0:
            count += 1
            if i != n/i:
                count +=1

    return count

divisors = 1
number = 1
tri_nums = []
target = 500
while divisors <= target:
    if number == 1:
        tri_nums.append(1)
    else:
        tri_nums.append(tri_nums[number-2] + number)

    curr_div = check_divisors(tri_nums[number-1])
    if curr_div > divisors:
        divisors = curr_div
        print divisors
    number += 1

print tri_nums[-1]

# print tri_nums
