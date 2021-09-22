import math
a=0
ans=-1
while a<1000:
    i=a
    while i<1000:
        temp=math.sqrt(a**2+i**2)
        if temp==int(temp) and a+i+temp==1000:
            ans=a*i*temp
            break
        i=i+1
    if ans>0: break
    a=a+1
print(ans)
