def nth_power_sum(n):
    ans = 0
    for num in range(10, 6*(9**5)):
        curr = 0
        k = num
        while k > 0:
            curr += (k%10)**n
            k = k//10
        ans = ans + curr if curr == num else ans
    return ans

print(nth_power_sum(5))
