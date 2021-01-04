# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 22:28:59 2020

@author: 융
"""
'''
[[-20,15], 
 [-14,-5], 
 [-18,-13], 
 [-5,-3]]
-20                          15      
    -18   -13
        -14      -5
                 -5    -3
-20 15
'''
def solution(routes):
    cnt = 1
    routes = sorted(routes,key=lambda x: x[0])
    rhtMin = routes[0][1]
    for r in routes:
        if rhtMin > r[1]:
            rhtMin = r[1]
        else:
            if rhtMin < r[0]:
                cnt += 1
                rhtMin = r[1]
        
    return cnt
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))