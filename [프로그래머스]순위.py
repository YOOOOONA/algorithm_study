def solution(n, results):
    answer = 0
    win = [set() for _ in range(n+1)]
    lose = [set() for _ in range(n+1)]
    # print(win)
    for i in range(1,n+1):
        for r in results:
            if r[0] == i:
                win[i].add(r[1])
            if r[1] == i:
                lose[i].add(r[0])
        li = lose[i].copy();lj = win[i].copy()
        for j in li:
            win[j].update(win[i])#i가 진 사람들에게 i가 이긴 사람 목록을 추가해줘야지?
        for j in lj:
            lose[j].update(lose[i])#i가 이긴사람들에게, i가 진사람들은 너넨 당연히 진다고 해줘야지
                
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
"""
[[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8]]
win
1:[2,3]
2:[3]
3:[4]
5:[6]
6:[7]
7:[8]

lose
2:[1]
3:[2]
4:[3]
6:[5]
7:[6]
8:[7]
"""