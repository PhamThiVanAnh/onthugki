# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:01:15 2024

@author: Administrator
"""
thang = int(input("Nhập vào tháng(1-12):"))
nam = int(input("Nhập vào năm:"))
if thang in ( 1,3,5,7,8,10,12):
    ngay = 31
elif thang in ( 4,6,9,11):
    ngay = 30    
if ( nam%4 ==0 and nam % 100 !=0) or ( nam % 400==0):
    ngay = 29
else: 
    ngay = 28    
print(f"{ngay}, {thang}, {nam}")