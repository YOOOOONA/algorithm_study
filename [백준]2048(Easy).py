import sys
from heapq import heappush,heappop
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

def move(dr,mat,N):
    #상하좌우로 쭉 밀리면서 더해지는 액션
    mvdMat = [[0 for _ in range(N)] for _ in range(N)]
    if dr in [0,1]:#상,하
        pm  = 1 if dr == 0 else -1
        for j in range(N):#가로줄로 탐색
            col = list(filter(lambda x:x!=0,list(zip(*mat))[j]))#0이 사이에 끼어있으면 지워줘야지
            n = len(col)
            newCol = []
            # for j in range(0,N-1,pm):
            i = 0 if pm == 1 else n-1
            while(n):                
                if 0<=i+pm<n and col[i]==col[i+pm]:#mat[i][j] == mat[i+pm][j]:
                    # newCol.append(mat[i][j] * 2)
                    newCol.append(col[i] * 2)
                    i += 2 * pm
                else:
                    # newCol.append(mat[i][j])
                    newCol.append(col[i])
                    i += 1 * pm

                if i<0 or i>=n: break#n==1일때 이 조건이 위에 있으면 안들어옴.무조건 한번은 들어와야지
            if pm==1:#상
                for i in range(0,len(newCol)):
                    mvdMat[i][j] = newCol[i]
            else:#하
                for i in range(0,len(newCol)):
                    mvdMat[N-1 -i][j] = newCol[i]
    if dr in [2,3]:#좌,우
        pm  = 1 if dr == 2 else -1
        for i in range(N):#가로줄로 탐색
            row = list(filter(lambda x:x!=0,mat[i]))#0이 사이에 끼어있으면 지워줘야지
            n = len(row)
            newRow = []
            # for j in range(0,N-1,pm):
            j = 0 if pm == 1 else n-1
            while(n):                
                if 0<=j+pm<n and row[j] == row[j+pm]:#mat[i][j] == mat[i][j+pm]:
                    # newRow.append(mat[i][j] * 2)
                    newRow.append(row[j] * 2)
                    j += 2 * pm
                else:
                    # newRow.append(mat[i][j])
                    newRow.append(row[j])
                    j += 1 * pm

                if j<0 or j>=n: break#n==1일때 이 조건이 위에 있으면 안들어옴.무조건 한번은 들어와야지
            if pm==1:#좌
                for j in range(0,len(newRow)):
                    mvdMat[i][j] = newRow[j]
            else:#우
                for j in range(0,len(newRow)):
                    mvdMat[i][N-1 -j] = newRow[j]
                
    # pm = 1 if dr in [0,2] else -1
    # for i in range(N)
    # I,J = i+pm,j if dr in [0,1] else i,j+pm
    
    return mvdMat

def calcMax(mat):
    maxNum = -1
    for i in mat:
        maxNum = max(maxNum,max(i))
    return maxNum

def solve(mat,N):
    maxNum = -1
    cnt = 0#회전한 횟수
    q = []
    heappush(q,[cnt,mat])
    # for _ in range(5):#최대 5번 이동
    while q:
        c,newMat = heappop(q)
        if c>=5:break
        for dr in range(4):
            mvdMat = move(dr,newMat,N)
            heappush(q,[c+1,mvdMat])
            maxNum = max(maxNum,calcMax(mvdMat))
    return maxNum#5번 이내로 이동해서 나오는 최댓값을 리턴



# N = int(input())
# mat = [list(map(int,input().split())) for _ in range(N)]
# if N == 1:
#         print(mat[0][0])
# else:
#     print(solve(mat,N))

while(True):
    try:
        N = int(input())
    except:
        break
    # if N != 1:continue
    mat = [list(map(int,input().split())) for _ in range(N)]
    if N == 1:
        print(mat[0][0])
    else:
        print(solve(mat,N))