def factorial(n):
    total = 1
    while n >= 1:
        total *= n
        n -= 1
    return total

def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

print(sum_digits(factorial(100)))
