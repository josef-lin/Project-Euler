def sum_mult_3_5(num):
    ans = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans

print(sum_mult_3_5(1000))
