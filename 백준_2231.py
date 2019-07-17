# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:03:16 2019

@author: 융
"""

#216=198+1+9+8
#256=245+2+4+5
#d=abc+a+b+c
import sys
init=int(input())

for a in range(1):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        for g in range(10):
                            if((a+b+c+d+e+f+g+(a*1000000+b*100000+c*10000+d*1000+e*100+f*10+g))==init):
                                print(a*1000000+b*100000+c*10000+d*1000+e*100+f*10+g)
                                sys.exit(0)
print(0)