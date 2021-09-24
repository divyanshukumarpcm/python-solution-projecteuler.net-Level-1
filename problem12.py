import math
max_divisor=0
i=1

def num_div(n):
    i=1
    count=0
    while i<=math.sqrt(n):
        if n%i==0: count=count+2
        i=i+1
    return count
while True:
    s=i*(i+1)/2
    if num_div(s)>500: print(s); break;
    i=i+1
