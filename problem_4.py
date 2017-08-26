## Probelm 4

res = []

def is_palindrome(n):
    """ Checks if an integer number (n) is a palindrome. """
    n_list = [int(i) for i in str(n)]
    reverse = n_list[:]
    reverse.reverse()
    if n_list == reverse:
        return True
    else:
        return False

for i in range(100,1000):
    for j in range(i,1000):
        if is_palindrome(i*j):
            res.append(i*j)

print max(res)
