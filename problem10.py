import math

def isprime(n):
    if n==0 or n==1: return False;
    if n==2 or n==3: return True
    if n%2==0 or n%3==0: return False;
    i=5
    while i<=math.sqrt(n):
        if n%i==0: return False
        i=i+1
    return True

j=0
sum=0
while j<2000000:
    if isprime(j):sum=sum+j
    j=j+1
print(sum)
