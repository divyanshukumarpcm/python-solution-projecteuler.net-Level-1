dic={
    "jan":31,
    "feb":28,
    "mar":31,
    "apr":30,
    "may":31,
    "jun":30,
    "jul":31,
    "aug":31,
    "sep":30,
    "oct":31,
    "nov":30,
    "dec":31,     
}

y=1901
count=0
days=1
while y<=2000:
    days=days+dic["jan"]
    if (days+1)%7==0: count=count+1;
    days=days+dic["feb"]
    if y%4==0: days=days+1
    if (days+1)%7==0: count=count+1;
    days=days+dic["mar"]
    if (days+1)%7==0: count=count+1;
    days=days+dic["apr"]
    if (days+1)%7==0: count=count+1;
    days=days+dic["may"]
    if (days+1)%7==0: count=count+1;
    days=days+dic["jun"]
    if (days+1)%7==0: count=count+1;
    days=days+dic["jul"]
    if (days+1)%7==0: count=count+1;
    days=days+dic["aug"]
    if (days+1)%7==0: count=count+1;
    days=days+dic["sep"]
    if (days+1)%7==0: count=count+1;
    days=days+dic["oct"]
    if (days+1)%7==0: count=count+1;
    days=days+dic["nov"]
    if (days+1)%7==0: count=count+1;
    days=days+dic["dec"]
    if (days+1)%7==0: count=count+1;
    y=y+1
print(count)
