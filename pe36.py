def reverse_int(num):
    ans = 0
    while num > 0:
        d = num%10
        ans = 10*ans + d
        num = num // 10
    return ans

def to_base2(num):
    if num == 0:
        return 0
    elif num % 2 == 0:
        num2 = 10*to_base2(num // 2)
    else:
        num2 = 1 + to_base2(num - 1)
    return num2
    

def sum_double_palindromes(n):
    total = 0
    for k in range(1, n):
        if reverse_int(k) == k and reverse_int(to_base2(k)) == to_base2(k):
            total += k
    
    return total

print(sum_double_palindromes(1000000))
