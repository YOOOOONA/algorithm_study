# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:23:01 2019

@author: 융
숫자가 적힌 문자열 numbers    "013"가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 
"""
'''
def solution(numbers):
    answer = 0
    
    numbers=list(map(int,numbers))
    for i in range(len(numbers))
    return answer
'''
numbers="123"
numbers=list(map(int,numbers))
print(numbers)
for i in range(len(numbers)):
    def newnum(n):#n은 numbers의 자릿수
        newnum=[]
        if(n==1):#자릿수가 한자리면 바꿀게 없지
            newnum=자기자신
        elif(n>1):#두자리수이상이면..123:1 2 3 
                                        12 21 13 31 23 32 
                                        1
                                          23 32
                                        2 
                                           13 31
                                        3  12  21
                                        
                                            
            newnum.append(newnum(n-1))
            if(num=)