
greatest=0
i=999

def pali(x):
    a=[]
    temp=x
    while temp!=0:
        a.append(temp%10)
        temp=int(temp/10)
    rev=0
    for i in a:
        rev=rev*10
        rev=rev+i
    if rev==x:
        return True
    else:
        return False

while i>=100:
    j=999
    while j>99:
        k=i*j
        if k>greatest and pali(k): greatest=k;
        j=j-1
    i=i-1
print(greatest)
