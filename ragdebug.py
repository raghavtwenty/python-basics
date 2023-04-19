# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:12:48 2019

@author: raghav
"""


# 03 oct 2019
import pdb
num_list = [500, 600, 700]
alpha_list = ['x', 'y', 'z']
x = 10
pdb.set_trace()


def nestedloop():
    for i in num_list:
        print(i)
    for j in alpha_list:
        print(j)


nestedloop()
