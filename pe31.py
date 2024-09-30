
coins = [1, 2, 5, 10, 20, 50, 100, 200]

def coin_sum(n, coin_types = 8):
    """ Counts the number of ways to make change using any number of coins

    >>> coin_sum(5)
    4
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif coin_types == 0:
        return 0
    
    return coin_sum(n-coins[coin_types-1], coin_types) + coin_sum(n, coin_types-1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(coin_sum(200))
