# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 03:51:51 2024

@author: Administrator
"""
import math
n = int(input("Nhập số nguyên dương: "))

if n < 2:
    print(n, "không phải là số nguyên tố")
else:
    kq = True
    for i in range(2, n-1 ):
        if n % i == 0:
            kq = False
            break
    if kq :
        print(n,"là số nguyên tố")
    else:
        print(n,"không phải là số nguyên tố")