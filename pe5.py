# finds a list of prime numbers, then finds the maximum power allowed
# multiply for smallest number divisible 

def primes_sieve(n):
    is_prime = [True]*(n+1) # excluding 0 and 1, true if prime
    p = 2
    while (p*p <= n):
        if (is_prime[p] == True): # check if it is a prime
            for i in range(p*p, n+1, p): 
                is_prime[i] = False # false if it is a multiple of p
        p += 1
    return [p for p in range(2, n+1) if is_prime[p]]

def smallest_mult(num):
    primes = primes_sieve(num)
    ans = 1
    for prime in primes:
        power = 1
        while prime ** (power+1) <= num:
            power += 1
        ans *= prime ** power
    return ans

print(smallest_mult(20))
