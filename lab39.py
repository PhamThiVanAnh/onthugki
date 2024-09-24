# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:43:30 2024

@author: VanAnh
"""
n = int(input("Nhập số nguyên dương n: "))

while n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
tong = 0
for i in range(1, n + 1):
    tong += 1 / i
print(tong)


