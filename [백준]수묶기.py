<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:10:52 2020

@author: 융
"""

def solution(seq):
    max_value = 0
    mult = 0
    cnt = 0
    mi = -1

    for i in range(len(seq)-1,-1,-1):
        if seq[i] > 1 and i == 0 and cnt == 0:
            max_value += seq[i]
            print(seq[i], max_value)
        if seq[i]>1:
            if cnt ==0:
                mult = seq[i]
                cnt+=1
            elif cnt == 1:
                max_value += mult * seq[i]
                print(seq[i], max_value)
                cnt = 0       
                mult = 0
        elif seq[i] == 1:
            if cnt == 0:
                max_value += 1
                print(seq[i], max_value)
            elif cnt == 1:
                max_value += mult + 1
                print(seq[i], max_value)
                mult = 0
            cnt = 0
        elif seq[i] == 0:
            max_value += mult
            mult = 0
        elif seq[i] < 0:
            mi = i
            break
    cnt = 0  
    if mi > 0:
        for i in range(0,mi+1):
            if cnt == 0:
                mult = seq[i]
                if i == mi:
                    if 0 in seq:
                        print(seq[i], max_value)
                        return max_value
                    else:
                        print(seq[i], max_value+mult)
                        return max_value + mult
                cnt += 1
            elif cnt == 1:
                max_value += mult * seq[i]
                print(seq[i], max_value)
                cnt = 0
    return max_value
    
if __name__=='__main__':
    N = int(input('N:'))#수열이 크기 10000미만
    seq= []
    for _ in range(N):
        seq.append(int(input()))#각 인풋값은 -10000이상 10000이하 정수
    seq = sorted(seq)
    ans = solution(seq)
=======
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:10:52 2020

@author: 융
"""

def solution(seq):
    max_value = 0
    mult = 0
    cnt = 0
    mi = -1

    for i in range(len(seq)-1,-1,-1):
        if seq[i] > 1 and i == 0 and cnt == 0:
            max_value += seq[i]
            print(seq[i], max_value)
        if seq[i]>1:
            if cnt ==0:
                mult = seq[i]
                cnt+=1
            elif cnt == 1:
                max_value += mult * seq[i]
                print(seq[i], max_value)
                cnt = 0       
                mult = 0
        elif seq[i] == 1:
            if cnt == 0:
                max_value += 1
                print(seq[i], max_value)
            elif cnt == 1:
                max_value += mult + 1
                print(seq[i], max_value)
                mult = 0
            cnt = 0
        elif seq[i] == 0:
            max_value += mult
            mult = 0
        elif seq[i] < 0:
            mi = i
            break
    cnt = 0  
    if mi > 0:
        for i in range(0,mi+1):
            if cnt == 0:
                mult = seq[i]
                if i == mi:
                    if 0 in seq:
                        print(seq[i], max_value)
                        return max_value
                    else:
                        print(seq[i], max_value+mult)
                        return max_value + mult
                cnt += 1
            elif cnt == 1:
                max_value += mult * seq[i]
                print(seq[i], max_value)
                cnt = 0
    return max_value
    
if __name__=='__main__':
    N = int(input('N:'))#수열이 크기 10000미만
    seq= []
    for _ in range(N):
        seq.append(int(input()))#각 인풋값은 -10000이상 10000이하 정수
    seq = sorted(seq)
    ans = solution(seq)
>>>>>>> 8912e574d4896c30f8fbe673f8374d993e5ac05e
    print("정답:",ans)