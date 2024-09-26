def primes_sieve(MAX_num):
    count = 0
    is_prime = [True]*(MAX_num+1) # excluding 0 and 1, true if prime
    p = 2
    while (p <= MAX_num):
        if (is_prime[p] == True): # check if it is a prime
            count += 1
            if count == 10001:
                return p
            for i in range(p*p, MAX_num+1, p):
                is_prime[i] = False # false if it is a multiple of p
        p += 1
    return None
    
print(primes_sieve(1000000))
