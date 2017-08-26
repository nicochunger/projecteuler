sqofsum = 0
sumofsq = 0

N = 100
for i in range(N+1):
    sumofsq += i**2
    sqofsum += i

sqofsum = sqofsum**2

print sqofsum - sumofsq
