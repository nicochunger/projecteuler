## Codigo para resolver el ejercicio 30 del Project Euler

res = []

for i in range(200000):
    numeros = [int(k) for k in str(i)]
    suma = 0
    for j in numeros:
        suma += j**5

    if suma == i:
        res.append(i)

print res
print sum(res)-1
