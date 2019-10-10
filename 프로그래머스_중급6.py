# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:25:36 2019

@author: 융
"""
#문자열 비교
def solution(nums):
    return str(int(''.join(sorted(list(map(str,nums)),key=lambda x: x*3, reverse=True))))
#퀵 소트
def max_(a,b):