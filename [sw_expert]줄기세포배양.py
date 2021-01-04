# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 10:30:16 2020

@author: 융
"""

import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    N,M,K = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]