# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:42:25 2020

@author: 융
"""
import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline
import copy

if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        #3<=N<=8, 1<=W<=5
        N, K = map(int, input().split())
        print(N)
        mat = [list(map(int, input().split())) for _ in range(N)]
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        dfs(0,mat)
        print("#{} {}".format(tc+1, blockCnts))