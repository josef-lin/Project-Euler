
def largest_prime_factor(n):
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
    return factors[-1] if factors else None
    
            
    
print(largest_prime_factor(600851475143))
