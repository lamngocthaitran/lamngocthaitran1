# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:46:21 2024

@author: lamngocthaitran
"""

print("giải phương trình bậc hai")
a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
c=float(input("Nhập số c:"))
D=b*b-4*a*c
if D==0:
    print("PT có nghiệm kép x1 = x2 =",-b/(2*a))
if D>0:
    print("PT có hai nghiệm x1=",(-b+D**0.5)/(2*a),"và x2=",(-b-D**0.5)/(2*a))
if D<0:
    print("PT vô nghiệm")
    
    