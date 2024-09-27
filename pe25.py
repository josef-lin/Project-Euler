import math

def Fibonacci_digits(k):
    phi = (1 + math.sqrt(5))/2
    # Fn asymptotically phi**n/math.sqrt(5)
    return math.ceil((math.log(math.sqrt(5), 10) + k-1 )/ math.log(phi, 10))
    
print(Fibonacci_digits(1000))
