import math
a=600851475143
b=math.sqrt(a)
i=int(b)+1
ans=a
def isprime(x):
    i=2
    p=True
    while i<=math.sqrt(x):
        if x%i==0: p=False;break;
        i=i+1
    return p
while i>0:
    if a%i==0 and isprime(i):
        break
    i=i-1
print(i)
