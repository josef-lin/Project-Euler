def reverse_int(num):
    ans = 0
    while num > 0:
        d = num%10
        ans = 10*ans + d
        num = num // 10
    return ans

def largest_prod():
    curr = 1
    for a in range(999,100,-1):
        for b in range(a,100,-1):
            num = a*b
            if reverse_int(num) == num:
                curr = max(curr,num)
    
    return curr

print(largest_prod())
