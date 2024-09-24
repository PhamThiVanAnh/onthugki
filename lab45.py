# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:32:01 2024

@author: VanAnh
"""

n = int(input("Nhập số n: "))
S=0
while n <=0:
    print("Nhap lai n:")
x = float(input("nhập x: "))
for i in range(1 , n+1 ):
        T=x**i
        M=i+1
        S= x + T/M
print(S)