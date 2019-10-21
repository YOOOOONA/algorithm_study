
N, M, V = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]#인접행렬의 인덱스를 있는그대로 받아오기 위해 행과열이0인건 안쓴다
for _ in range(M):
    i,j = map(int, input().split())
    matrix[i][j] = 1
    matrix[j][i] = 1


def dfs(current_node, row, foot_prints):
    foot_prints += [current_node]
    for search_node in range(1,N+1):
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)#재귀
    return foot_prints


def bfs(start):
    queue = [start]#bfs는 큐
    foot_prints = [start]
    while queue:
        current_node = queue.pop(0)#bfs는 다 큐에 떄려넣고 하나씩 꺼내서 그거의 이웃 또 떄려넣고
        for search_node in range(1,N+1):
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints

print(*dfs(V, matrix, []))#*붙여야 원소만 뽑아져나옴
print(*bfs(V))

'''
###################################################
#파이썬에서 asterisk(*)의 활용
1.list나 tuple unpacking

2.가변적인 키-밸류 인자 받기
def adder(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print("{} is {}".format(key,value))

num = {"arg3":3,"arg2":2,"arg1":5}
print(adder(**num))

>>>{"arg3":3,"arg2":2,"arg1":5}
>>>arg3 is 3
>>>arg2 is 2
>>>arg1 is 1

3.가변적인 파라미터 받기
def test_args(*args):
    print(args)
    print(args[0])
    print(type(args))

args = ("two",3,5)
test_args(*args)

'''