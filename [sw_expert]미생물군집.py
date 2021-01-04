<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:14:47 2020

@author: 융
"""

#import sys
#input = sys.stdin.readline

#list는 hashable하지 않아서 set안먹히는데 튜플은 됨

import sys
sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline

dr = [(-1,0),(+1,0),(0,-1),(0,+1)]

def solution(N , M , K , cases):
    #mat = [[1 if i in [0,N-1] or j in [0,N-1] else 0 for j in range(N)] for i in range(N)]#닿으면 안되는 테두리는 1로 셋팅
    for _ in range(M):#M시간동안
        mat = []
        for case in cases:#dr=1,2,3,4=상,하,좌,우=[(-1,0),(+1,0),(0,-1),(0,+1)]
            
            idx = case[3] - 1
            #print('이동 전:',case[:2])
            case[0] += dr[idx][0]; case[1] += dr[idx][1]
            #print('이동 후:',case[:2])
            if case[0] == 0: case[3] = 2; case[2] = case[2] // 2  #미생물 수 반내림
            elif case[0] == N-1: case[3] = 1; case[2] = case[2] // 2
            elif case[1] == 0: case[3] = 4; case[2] = case[2] // 2
            elif case[1] == N-1: case[3] = 3; case[2] = case[2] // 2
            #print(case)
            if case[2] != 0: mat.append(case)
            
        tmpCases = mat.copy()
        #print('tmpCases',len(tmpCases))
        #군집 두개 이상이 만나면 개수 합쳐지고 큰 놈의 방향을 따르기..근데 그런 놈이 여러 그룹일수있음(일단 그생각은 보류)
        comp = [tuple(li[:2]) for li in tmpCases]
        #print('?',comp)#,set(comp))
    
        while(len(set(comp)) != len(comp)):# 군집 두개 이상이 만나고 있다는 소리
            
            #for idx,gr in enumerate(tmpCases):
            idx = 0
            while(True):
                if idx < len(tmpCases):
                    gr = tmpCases[idx]
                else: break
            
                cases = []
                tmpLoc = gr[:2]
                
                num = gr[2]#미샐물 수
                tmpIdxs = [idx,]#중복이 되는 tmpCases의 케이스의 인덱스들 모으기
                tmpDir = gr[3]#큰놈의 방향을 넣을 것
                maxIdx = idx#큰 놈의 인덱스
                for kth in range(idx + 1, len(tmpCases)):
                    if tmpLoc == tmpCases[kth][:2]:
                        num += tmpCases[kth][2]
                        #print(tmpLoc, tmpCases[kth][:2],'같은거있음',num)
                        tmpIdxs.append(kth)
                        if tmpCases[maxIdx][2] < tmpCases[kth][2]:                            
                            maxIdx = kth
                tmpDir = tmpCases[maxIdx][3]
                #print('이게 잘못',[*tmpLoc,num,tmpDir],'\n')
                cases.append([*tmpLoc,num,tmpDir])
                
                rangeSet = set([i for i in range(0,len(tmpCases))])
                #print(idx,"범위",(rangeSet - set(tmpIdxs)))
                for gg in list((rangeSet - set(tmpIdxs))):
                    cases.append(tmpCases[gg])
                #print('ㄱㄱㄱ',cases)
                tmpCases = cases.copy()
                #print('tmpCases?',tmpCases)
                
                
                idx += 1;
                
            comp = [tuple([li[0],li[1]]) for li in tmpCases]
            #print('comp',comp)
            #break
        cnt = 0
        for c in tmpCases:
            cnt += c[2]
    return cnt#M시간 뒤 남은 총 미생물 합
    

if __name__ == '__main__':
    #T = map(int,input().split())
    T = int(input())
    #print()
    for i in range(1,T+1):
        N, M, K = map(int,input().split())#N,M,K = 한 변 길이, 격리 시간, 군집 수
        cases = [list(map(int,input().split())) for _ in range(K)]
        #print(cases)
                #이 리스트는 list = [i,j,num,dr] = [세로,가로,미생물 수,진행방향]
        #break
        print('#%d %d' %(i,solution(N,M,K,cases)))
    
'''
mat = [[0 if i==j else 1 for i in range(3)] for j in range(3)]
print(mat)

tu = tuple([1,2])
print(tu,type(tu))

li = [range(0,9)]
print(li)
li = set([i for i in range(0,9)])
for i in li:
    print(i)
'''
=======
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:14:47 2020

@author: 융
"""

#import sys
#input = sys.stdin.readline

#list는 hashable하지 않아서 set안먹히는데 튜플은 됨

import sys
sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline

dr = [(-1,0),(+1,0),(0,-1),(0,+1)]

def solution(N , M , K , cases):
    #mat = [[1 if i in [0,N-1] or j in [0,N-1] else 0 for j in range(N)] for i in range(N)]#닿으면 안되는 테두리는 1로 셋팅
    for _ in range(M):#M시간동안
        mat = []
        for case in cases:#dr=1,2,3,4=상,하,좌,우=[(-1,0),(+1,0),(0,-1),(0,+1)]
            
            idx = case[3] - 1
            #print('이동 전:',case[:2])
            case[0] += dr[idx][0]; case[1] += dr[idx][1]
            #print('이동 후:',case[:2])
            if case[0] == 0: case[3] = 2; case[2] = case[2] // 2  #미생물 수 반내림
            elif case[0] == N-1: case[3] = 1; case[2] = case[2] // 2
            elif case[1] == 0: case[3] = 4; case[2] = case[2] // 2
            elif case[1] == N-1: case[3] = 3; case[2] = case[2] // 2
            #print(case)
            if case[2] != 0: mat.append(case)
            
        tmpCases = mat.copy()
        #print('tmpCases',len(tmpCases))
        #군집 두개 이상이 만나면 개수 합쳐지고 큰 놈의 방향을 따르기..근데 그런 놈이 여러 그룹일수있음(일단 그생각은 보류)
        comp = [tuple(li[:2]) for li in tmpCases]
        #print('?',comp)#,set(comp))
    
        while(len(set(comp)) != len(comp)):# 군집 두개 이상이 만나고 있다는 소리
            
            #for idx,gr in enumerate(tmpCases):
            idx = 0
            while(True):
                if idx < len(tmpCases):
                    gr = tmpCases[idx]
                else: break
            
                cases = []
                tmpLoc = gr[:2]
                
                num = gr[2]#미샐물 수
                tmpIdxs = [idx,]#중복이 되는 tmpCases의 케이스의 인덱스들 모으기
                tmpDir = gr[3]#큰놈의 방향을 넣을 것
                maxIdx = idx#큰 놈의 인덱스
                for kth in range(idx + 1, len(tmpCases)):
                    if tmpLoc == tmpCases[kth][:2]:
                        num += tmpCases[kth][2]
                        #print(tmpLoc, tmpCases[kth][:2],'같은거있음',num)
                        tmpIdxs.append(kth)
                        if tmpCases[maxIdx][2] < tmpCases[kth][2]:                            
                            maxIdx = kth
                tmpDir = tmpCases[maxIdx][3]
                #print('이게 잘못',[*tmpLoc,num,tmpDir],'\n')
                cases.append([*tmpLoc,num,tmpDir])
                
                rangeSet = set([i for i in range(0,len(tmpCases))])
                #print(idx,"범위",(rangeSet - set(tmpIdxs)))
                for gg in list((rangeSet - set(tmpIdxs))):
                    cases.append(tmpCases[gg])
                #print('ㄱㄱㄱ',cases)
                tmpCases = cases.copy()
                #print('tmpCases?',tmpCases)
                
                
                idx += 1;
                
            comp = [tuple([li[0],li[1]]) for li in tmpCases]
            #print('comp',comp)
            #break
        cnt = 0
        for c in tmpCases:
            cnt += c[2]
    return cnt#M시간 뒤 남은 총 미생물 합
    

if __name__ == '__main__':
    #T = map(int,input().split())
    T = int(input())
    #print()
    for i in range(1,T+1):
        N, M, K = map(int,input().split())#N,M,K = 한 변 길이, 격리 시간, 군집 수
        cases = [list(map(int,input().split())) for _ in range(K)]
        #print(cases)
                #이 리스트는 list = [i,j,num,dr] = [세로,가로,미생물 수,진행방향]
        #break
        print('#%d %d' %(i,solution(N,M,K,cases)))
    
'''
mat = [[0 if i==j else 1 for i in range(3)] for j in range(3)]
print(mat)

tu = tuple([1,2])
print(tu,type(tu))

li = [range(0,9)]
print(li)
li = set([i for i in range(0,9)])
for i in li:
    print(i)
'''
>>>>>>> 8912e574d4896c30f8fbe673f8374d993e5ac05e
