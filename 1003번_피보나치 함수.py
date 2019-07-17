# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:59:25 2019

@author: 융
"""
'''
N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램
입력
3//testcase
0
1
3
출력
1 0//0출력횟수 1출력횟수
0 1
1 2
29056 KB	64 ms
'''


'''
def fibonacci(n):
    fibonacci=[0]*n
    if (n == 0):
        cnt0+=1
        print(cnt0, cnt1)
        return 0
    elif (n == 1):
        cnt1+=1
        print(cnt0, cnt1)
        return 1
    else:
        fib = fibonacci(n‐1) + fibonacci(n‐2)
        return fib
        
'''
'''
memo = {1:1, 2:1}#이건 뭐지
cnt0=0
cnt1=0
def fibonacci(n):
    if n == 0:
        cnt0+=1
        print(cnt0, cnt1)
        return 0
    if n not in memo:
        if(n==1):
            cnt1+=1
        print(cnt0, cnt1)
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]    
t=int(input())

for i in range(t):
    

    n=int(input())
    fibonacci(n)
    
'''
def count_fibonacci(n):
    zero_count = [1,0]
    one_count = [0,1]
    if n <= 1:
        return
 
    for i in range(2, n+1):
        zero_count.append(zero_count[i-1] + zero_count[i-2])
        one_count.append(one_count[i-1] + one_count[i-2])
 
    return zero_count, one_count
 
n = int(input())
zero_count, one_count = count_fibonacci(40)
 
for _ in range(n):
    m = int(input())
    print("%d %d" % (zero_count[m], one_count[m]))
 
