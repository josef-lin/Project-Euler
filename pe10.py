def sum_primes_sieve(MAX_num):
    ans = 0
    is_prime = [True]*(MAX_num+1) # excluding 0 and 1, true if prime
    p = 2
    while (p <= MAX_num):
        if (is_prime[p] == True): # check if it is a prime
            ans += p
            for i in range(p*p, MAX_num+1, p):
                is_prime[i] = False # false if it is a multiple of p
        p += 1
    return ans
    
print(sum_primes_sieve(2000000))
