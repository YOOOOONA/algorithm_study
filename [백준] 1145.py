# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:17:10 2020

@author: 융
"""
#   import sys
m=list(map(int,input().split()))#5개 100미만 정수
#적어도 대부분의 배수 구하기 :최소 3개로 나눌수 있는 가장 작은 자연수

li=[]
for num in m:
    mat=m[:]
    mat.remove(num)
    print("mat:",mat)
    cnt=0
    i=2
    im=0
    while(im==0):
        for j in mat:
            nn=num*i
            print(nn)
            if nn%j==0:
                print(nn,"나눠짐",j)
                cnt+=1
            if cnt>=2:
                print(nn)
                im=1
                li.append(nn)
                print("li:",li)
                break
        cnt=0
        i+=1
print(min(li))
#30 42 70 35 90