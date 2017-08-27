# Problem 9

N = 1000
for i in range(1000):
    for j in range(i+1,1000):
        for k in range(j+1,1000):
            if i**2+j**2 == k**2:
                if i+j+k == 1000:
                    print (i, j, k)
                    print i*j*k
                    break
                    break
                    break
            continue
