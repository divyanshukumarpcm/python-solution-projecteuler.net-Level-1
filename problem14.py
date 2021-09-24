#My favourite collatz conjecture - BUT DO NOT WASTE YOUR TIME ON THIS THEOREM
#probably russian created it to waste time of americans and slow progrees

def collatz_count(n):
    count=0
    while n!=1:
        if n%2==0: n=n/2
        else: n=3*n+1
        count=count+1
    return count

i=1
max_index=i
max_count=0
while i<1000000:
    if collatz_count(i)>max_count: max_index=i;max_count=collatz_count(i);
    i=i+1
print(max_index," ",max_count)
