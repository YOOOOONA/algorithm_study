# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:40:49 2020

@author: 융
"""
#이진탐색
#숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 
#정수 M개가 주어졌을 때, 
#이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
'''
input
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10

output 
1 0 0 1 1 0 0 1
'''
def find(have, i, low, high):
    if low > high:
        print("0", end = " ")
        return
    mid = (low+high)//2
    if have[mid] == i:
        print("1" , end = " ")
        return
    elif have[mid] < i:
        find(have, i, mid+1, high)
    elif have[mid] > i:
        find(have, i, low, mid-1)       

def solution(N,have,M,target):#have는 정렬돼있음
    ans = []#가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력
    for i in target:
        find(have, i, 0, N-1)

if __name__ == "__main__":
    N = int(input())#1이상 50만 이하 상근이가 가진 카드 개수
    have = list(map(int,input().split()))# -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 
                                 #두 숫자 카드에 같은 수가 적혀있는 경우는 없다.
    M = int(input())#1이상 50만 이하 찾아야할 카드 개수
    target = list(map(int,input().split()))
    
    ans = solution(N,sorted(have),M,target)

