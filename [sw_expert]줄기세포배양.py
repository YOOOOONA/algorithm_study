<<<<<<< HEAD
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
=======
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
>>>>>>> 8912e574d4896c30f8fbe673f8374d993e5ac05e
    mat = [list(map(int,input().split())) for _ in range(N)]