# Problem 16

n = 2**1000

str_n = str(n)

total_sum = 0
for i in str_n:
    total_sum += int(i)

print total_sum
