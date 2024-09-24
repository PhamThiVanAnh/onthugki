# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:56:44 2024

@author: VanAnh
"""
n = int(input("Nhập vao n: "))
S=0
while n <= 0:
    n = int(input("Nhập lai n: "))
for i in range(1 , n+1 ):
            S= (2*i - 1) / (2*i)
print(S)