# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:07:37 2024

@author: VanAnh
"""
danhsach=[]
max=0
for x in range (1,490):
    for y in range (1,140):
        for z in range (1,109):
            if 2*x + 7*y + 9*z==979:
                sum= x+y+z
                if sum>max:
                    max=sum
                    danhsach=[(x,y,z)]
print(f"{danhsach} voi bo nghiem (x+y+z)={max}")