<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:57:17 2020

@author: 융
"""

def solution(a):
    answer = 1
    M = min(a)
    for _ in range(2):
        m = a[0]
        for i in range(1,len(a)):
            if m > M and m >= a[i]:
                m = a[i]
                answer += 1
            elif m==M: break
        a.reverse()
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:57:17 2020

@author: 융
"""

def solution(a):
    answer = 1
    M = min(a)
    for _ in range(2):
        m = a[0]
        for i in range(1,len(a)):
            if m > M and m >= a[i]:
                m = a[i]
                answer += 1
            elif m==M: break
        a.reverse()
>>>>>>> 8912e574d4896c30f8fbe673f8374d993e5ac05e
    return answer