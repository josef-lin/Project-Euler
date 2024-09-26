def sum_even_fib(num):
    ans = 2
    a = 1
    b = 2
    while b<num:
        c = a+b
        a = b
        b = c
        if b%2==0:
            ans+=b
    return ans

print(sum_even_fib(4000000))
