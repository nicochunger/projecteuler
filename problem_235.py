# Problem 235

def serie(r, k):
    return (900-3*k)*r**(k-1)

def suma(n, r):
    suma = 0
    for i in range(n):
        suma += serie(r,i+1)

    return suma

n = 5000

gol = -600000000000

r = 1.0023
d1 = r
d2 = 1.0024

while len(str(r)) < 15:
    d = (d1+d2)/2
    if suma(n, d) > gol:
        d1 = d
    else:
        d2 = d
    r = d

print r
