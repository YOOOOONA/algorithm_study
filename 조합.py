# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 00:28:28 2020

@author: 융
"""

def recursion(l1,l2,arr):
    arr.append(l1)
    for i,x in enumerate(l2):
        recursion(l1 + [x], l2[i+1:], arr)#l1 + [x]한거는 arr에 계속 들어감
def combination(l):
    result = []
    recursion([],l,result)
    return result[1:]#왜냐면 맨 첫번쨰에는 공집합일 테니까
print(combination([1,2,3]))