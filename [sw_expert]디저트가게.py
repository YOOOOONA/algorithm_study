
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 20:15:40 2020

@author: 융
"""

import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline
import copy
'''
def recur(sp,way,now,rot):
    global largest
    print('before',sp,now,way,rot)
    if 0<=now[0]+dy[rot]<N and 0<=now[1]+dx[rot]<N:
        
        now[0] += dy[rot]; now[1] += dx[rot]
        if mat[now[0]][now[1]] not in way:
            way.append(mat[now[0]][now[1]])
            print('after',sp,now,way,rot)
        else:
            if sp == now:
                largest = max(largest,len(way))#가장 많이 먹은 때의 경로길이 출력
                print('정답2',way,largest)
                return
        if sp == now and len(way)>4 and (len(way)-1 == len(set(way)))  and way[0] == way[-1]:
            
            largest = max(largest,len(way)-1)#가장 많이 먹은 때의 경로길이 출력
            print('정답1',way,largest)
            #print('아님 여기?',way)
            return
        if sp != now and (len(way) != len(set(way))) :print('중복나옴');return
        #print(way,now,rot)
        if rot == 0:
            recur(sp,way,now,0)
            recur(sp,way,now,1) 
            recur(sp,way,now,2)
            recur(sp,way,now,3)
        elif rot == 1:
            recur(sp,way,now,1)
            recur(sp,way,now,2)
            recur(sp,way,now,3)
        elif rot == 2:
            recur(sp,way,now,2)
            recur(sp,way,now,3)
        elif rot == 3:
            recur(sp,way,now,3)
        way.remove(mat[now[0]][now[1]])
    else:
        print('나옴')
        return

def solution():
    global largest
    
    for i in range(N):
        for j in range(N):
            sp = [i,j]
            #print(sp)
            way = [mat[i][j],]
            now = [i,j]
            rot = 0
            #print(way)
            recur(sp,way,now,rot)
            

if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        #4<=N<=20
        N = int(input())
        #디저트 종류 1이상 100이하. 같은 숫자 칸 못 지나감.한번씩만 갈수있음.출발한 카페로 돌아와야됨.대각선으로만 갈 수 있음.
        mat = [list(map(int, input().split())) for _ in range(N)]
        dx = [-1,1,1,-1]
        dy = [1,1,-1,-1]
        
        largest = -1#디저트를 못먹으면 -1임
        solution()
        print("#{} {}".format(tc+1, largest))
        break
'''
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

#k는 방향, n은 진행한 칸수
def f(i,j,k,n): 
    global si,sj,maxV
    #출발점에 도착한경우
    #print('before',si,sj,'|now',i,j,'|',k,U)
    if k == 3 and i == si and j == sj: 
        if maxV < n:
            maxV = n
    elif i<0 or i>=N or j<0 or j>=N:
        return
    #숫자가 겹친경우
    elif arr[i][j] in U: 
        return
    else:
        U.append(arr[i][j])
        #print('after',si,sj,'|now',i,j,'|',k,U)
        #오른쪽 방향 그대로 가거나 왼쪽으로 꺾었을 경우에
        if k == 0 or k ==1:
            f(i+di[k],j+dj[k],k,n+1)
            #k+1방향
            f(i+di[k+1],j+dj[k+1],k+1,n+1)
        elif k ==2:
            #출발점을 향하는게 아님
            #if i!=si or j!=sj:
            if i+j != si+sj:#도착할 가능성이 없는 경우

                f(i+di[2], j+dj[2],k,n+1)
            else:#도착할 가능성이 있는 경우
                print(i,j,si,sj)
                f(i+di[3],j+dj[3],k+1,n+1)
        #k가 3일때는 직진한다.
        else:
            f(i+di[3],j+dj[3],k,n+1)
 
        U.remove(arr[i][j])
 
 
T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    maxV = -1
    U = []
    for i in range(N):
        for j in range(1,N-1):
            si = i
            sj = j
            U.append(arr[i][j])
            f(i+1,j+1,0,1)
            U.remove(arr[i][j])
 
    print("#{} {}".format(tc+1, maxV))
