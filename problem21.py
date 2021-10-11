#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 20:41:11 2021

@author: Divyanshu Kumar
"""

import math

#function to calculate sum of proper divisors
def divsum(n):
    temp=0
    i=1
    while i<=math.sqrt(n):
        if n%i==0:
            temp=temp+i
            if i!=1:
                temp=temp+int(n/i)
        i=i+1
    return temp

#calculate all number's divisor sum and store in array
i=1
sm=[0]
while i<10000:
    sm.append(divsum(i))
    i=i+1


#check for which pair of numbers amicable sum is satisfied and storing in dictionary so that values do not get repeated
amc_sum={}
j=1
while j<10000:
    t=sm[j]
    if sm[j]>10000:
        asdf=divsum(sm[j])   # a few numbers 'b' can be greater than 10000, so calculating divisor sum for them them also
    else:
        asdf=sm[t] 
    if asdf==j and t!=j:
            amc_sum[j]="1"
            amc_sum[t]="1"
    j=j+1

# print(amc_sum)

ans=0
for i in amc_sum.keys():
    ans=ans+i
print(ans)
