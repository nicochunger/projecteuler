# Problem 5
res = []
n = 20
for i in range(0, 1000000000, 1140):
    if i == 0:
        continue
    count = 0
    for j in range(1,n+1):
        if i%j != 0:
            break
        count += 1
    if count == n:
        res.append(i)

print min(res)
