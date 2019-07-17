# -*- coding: utf-8 -*-
"""
Created on Fri May 24 01:25:35 2019

@author: 융
"""
'''
2×n 직사각형을 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램

입력
2//n     8            12
        
출력
3       171           2731
'''
'''
1

11
22
 4

111
122
1 4

1111
1122
11 4
22 4
 4  4

11111
11122
111 4
122 4
1 4 4

111111
111122
1111 4
112222
1122 4
11 4 4
222222
2222 4
22 4  4
4  4  4

1111111
1111122
11111  4
1112222
11122  4
111 4  4
1222222
12222 4
122 4  4
1 4  4  4
'''#11->22->4가능
'''
import itertools

n=int(input())
tile=['a']*n
i=0
j=0
while(True):
    i+=1
    if tile[i]=='a' and tile[i+1]=='a':
        #aa를 b하나로 바꿈 어떻게? a->b하고 a하나는 delete->aaaaa, baaaa,bbaa,bbb이거 세개 permutation해야될거같은데
while(True):
    j+=1
    if(tile[j]=='b'):
        #b는 c로 바꿀 수 있게!  caaaa,ccaa,ccc
    mypermuatation =  itertools.permutations(tile)
        
   '''
   '''
i-1칸까지 채운 뒤, 1X2 타일을 하나 세로로 채우는 경우
i-2칸까지 채운 뒤, 2X1 타일을 위 아래로(가로) 2개 채우는 경우
i-2칸까지 채운 뒤, 2X2 타일을 하나 채우는 경우
i-2 칸까지 채운 경우 2가지로 나뉘기 때문에
d[i-2] * 2 를 해주면 된다.

d[i] = d[i-1] + d[i-2]     
        '''

n = int(input())
d = [0,1,3]
 
for i in range(3,n+1):
    d.append(d[i-1] + (2 * d[i-2]))
 
print(d[n] % 10007)
        
        
        
        
        
        