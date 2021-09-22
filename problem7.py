import math
x=10001

i=2

def isprime(z):
    if z==2 or z==3: return True
    if z%2==0: return False
    if z%3==0: return False
    p=True
    i=5
    while i<=math.sqrt(z):
        if z%i==0: return False
        i=i+1
    return True

while x>0:
    if isprime(i): x=x-1
    i=i+1
print(i-1)
