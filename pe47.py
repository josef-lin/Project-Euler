def unique_prime(n):
    """ Returns number of unique prime factors of n

    >>> unique_prime(51) # 3 * 17
    2
    >>> unique_prime(27) # 3 ** 3
    1
    >>> unique_prime(120) # (2 ** 3) * 3 * 5
    5
    """
    k = smallest_factor(n)
    def no_k(n):
        """ Returns the number of unique prime factors of n other than k
        """
        if n == 1:
            return 0
        elif n % k != 0:
            return unique_prime(n)
        else:
            return no_k(n//k)
    return 1 + no_k(n)

def smallest_factor(n):
    """ Returns the smallest prime factor of n """
    if n == 1:
        return None
    k = 2
    while k <= n:
        if n % k == 0:
            return k
        k += 1

i = 2
count = 0
target = 4
while count < target:
    if unique_prime(i) != target:
        count = 0
    else:
        count += 1
    i += 1

print(i - (target))
