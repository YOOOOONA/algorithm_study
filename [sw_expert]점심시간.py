# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:22:01 2020

@author: 융
"""

import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline

def recur(l1,l2,arr):
    arr.append(l1)
    for i,x in enumerate(l2):
        recur(l1 + [x], l2[i+1:], arr)
        
def combination(li):#명단 있을 때 가능한 조합 모두 구하기
    result = []
    recur([], li, result)
    return result[1:]

def compute(Pq1, S1, Pq2, S2):#Pq1 = [[0:1번계단까지의 0번 사람의 거리+계단 길이],,,]
    tt1 = tt2 = 0
    Pq1 = sorted(Pq1, key = lambda x : x[1])
    print('Pq1:',Pq1)
    while Pq1:
        for i in range(len(Pq1)):
            if Pq1[i][1] == 0:
                Pq1.pop(0)
                print('Pq1:',Pq1)
            elif Pq1[i][1] > S1 or (Pq1[i][1] == S1 and i < 2):
                Pq1[i][1] = Pq1[i][1] - 1
                print('Pq1:',Pq1)
            elif Pq1[i][1] == S1:
                continue
        tt1 += 1
    
    Pq2 = sorted(Pq2, key = lambda x : x[1])
    while Pq2:
        for i in range(len(Pq2)):
            if Pq2[i][1] == 0:
                Pq2.pop(0)
            elif Pq2[i][1] > S2 or (Pq2[i][1] == S2 and i < 2):
                Pq2[i][1] = Pq2[i][1] - 1
            elif Pq2[i][1] == S2:
                continue
        tt2 += 1
    return max(tt1,tt2)
    
def solution(N,mat):
    tMin = 99999999999999
    pList = []
    sList = []
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1: pList.append([i,j])
            elif mat[i][j] > 1: sList.append([i,j])
    print(pList,sList)
    #모든 사람 다 각 계단에 할당하기.계단은 반드시 두개
    #i는 1번째 계단에 할당할 사람의 수 , len(pList)-i가 2로 가겠지
        #사람 수를 정했으니 누구를 할당할지 정해야지
    idxList = [i for i in range(len(pList))]#사람에게 인덱스 붙이기
    
    psComb = combination(idxList)#[[0],[1],[2],[0,1],,,]
    S1 = mat[sList[0][0]][sList[0][1]]#1계단의 길이
    S2 = mat[sList[1][0]][sList[1][1]]#2계단의 길이
        
    for p in psComb:#각 사람들의 인덱스를 계단 1 또는 2에 할당 시켜야됨
        #p에 있으면 1계단, 없으면 2계단에 할당하기
        P1 = p#[1,3,4]
        Pq1 = [[x,abs(sList[0][0]-pList[x][0]) + abs(sList[0][1]-pList[x][1]) + S1] for x in P1]
        P2 = list(set(idxList)-set(P1))
        print(P1,P2)
        Pq2 = [[x,abs(sList[1][0]-pList[x][0]) + abs(sList[1][1]-pList[x][1]) + S2] for x in P2]
        tt = compute(Pq1, S1, Pq2, S2)
        tMin = min(tMin,tt)
        print(tMin)
        
    return tMin#모든이가 계단을 내려가는 최단시간 리턴

if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        N = int(input())#4이상 10이하의 매트릭스사이즈
        mat = [list(map(int,input().split())) for _ in range(N)]#계단이 있는지 사람이 있는지
        tm = solution(N,mat)
        print("#{} {}".format(tc+1, tm))