# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:47:04 2024

@author: VanAnh
"""
n = int(input("Nhập vao n: "))
S=0
while n <= 0:
    n = int(input("Nhập lai n: "))
for i in range(1 , n+1 ):
            S+= i / (i+1)
print(S)