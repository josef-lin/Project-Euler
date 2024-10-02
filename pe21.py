
def amicable_numbers(n):
    keys = range(1,n)
    vals = [0]*(n-1)
    factor_sum = dict(zip(keys, vals))
    for i in keys:
        for k in keys:
            if k % i == 0 and k != i:
                factor_sum[k] += i

    valid_keys = []
    for a in keys:
        if factor_sum[a] in keys and factor_sum[a] != a and a == factor_sum[factor_sum[a]]:
            valid_keys.append(a)
    print(valid_keys)
    return sum(valid_keys)

print(amicable_numbers(10000))

