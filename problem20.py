#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 20:41:11 2021

@author: Divyanshu Kumar
"""

#program to print sum of factorial of all numbers
mega={}
def fact(n):
    if n==0: return 1
    if n in mega.keys():
        return mega[n]
    else: 
        temp=n*fact(n-1)
        mega[n]=temp
        return temp
for i in range(101):
    a=str(fact(i))
    
    su=0
    for j in a:
        su=su+int(j)
    if(i==100): print(i," ",su)
