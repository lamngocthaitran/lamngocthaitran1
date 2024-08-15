# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:37:33 2024

@author: lamngocthaitran
"""

print("giải phương trình bậc nhất")
print("giải phương trình bậc nhất")
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print("Nghiệm của phương trình là: {:.4f}".format(x))