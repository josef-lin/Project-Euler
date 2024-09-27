def longest_collatz(N):
    known = {1:1, 2:2, 4:3}
    i = 3
    longest_chain_length = 3
    ans = 4
    while i <= N:
        curr = 0
        n = i
        while n not in known:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3*n+1
            curr += 1
        known[i] = curr + known[n]
        if known[i] > longest_chain_length:
            longest_chain_length = known[i]
            ans = i
        i += 1
    return ans
    
print(longest_collatz(1000000))
