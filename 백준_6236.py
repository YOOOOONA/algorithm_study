# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:23:03 2019

@author: 융
"""
string=[]
while True:
    input_data=int(input())
    if input_data=='':
        break
    else:
        string.append(input_data)
    string.sort()
    
    for line in string:
        #print(line,end=" ")
        
t=int(input())
n,m=map(int,input().split())
for i in range(t):
    for j in range(m):
        
        
        
1,2  1,3  1,4  1,5
1,2  2,3  3,1  1,4 4,2 2,5