def solution(n, results):
    answer = 0
    win = {}
    lose = {}
    for i in range(1,n+1):
        win[i]=set()
        lose[i]=set()
    # print(win)
    for i in range(len(results)):
        win[results[i][0]].add(results[i][1])
        lose[results[i][1]].add(results[i][0])
    # print(lose)
    for i in range(1,n+1):
        li = win[i].copy();lj = lose[i].copy()
        for j in li:
            win[i].update(win[j])
        for j in lj:
            lose[i].update(lose[j])
            
    # print(win,'\n',lose)
    for i in range(1,n+1):
        if len(win[i]) + len(lose[i])==n-1:
            answer += 1
    return answer#정확하게 순위를 매길 수 있는 선수의 수
"""
win
[
    1:[2,5]
    2:[5]
    3:[2,5]
    4:[2,3,5]
    
]
lose[
    2:[1,3,4]
    3:[4]
    5:[2,1,3,4]
]
"""
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))