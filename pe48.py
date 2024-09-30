
def mod_power(b,p,m):
    if p == 1:
        return b % m
    elif p % 2 == 1:
        return (b * mod_power(b,(p-1)//2,m)**2) % m
    else:
        return (mod_power(b, p//2, m)**2) % m

def self_powers(n, m):
    ans = 0 
    for i in range(1, n+1):
        ans = (ans + mod_power(i,i,m)) % m
    return ans

print(self_powers(1000, 10**10))
