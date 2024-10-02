import numpy as np

def number_prime_factor(n):
    p = 2
    factors = []
    multiplicity = []
    while p <= n:
        if n % p == 0:
            if p in factors:
                multiplicity[-1] += 1
            else:
                factors.append(p)
                multiplicity.append(1)
            n = n//p
        else:
            p += 1
    if factors:
        return np.prod(np.array(multiplicity)+1)
    return 1


i = 1
tri = 1
while number_prime_factor(tri) < 500:
    i += 1
    tri += i
    
print(tri)
