# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 02:04:18 2020

@author: 융
"""

import math
a, b = input().split()
a = int(a)
b = int(b)
result = 1 + math.ceil((a - b) / (b-1))
print(result)