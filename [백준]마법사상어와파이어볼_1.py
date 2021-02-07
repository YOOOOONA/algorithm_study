#시간초과
dx = [0,1,1,1,0,-1,-1,-1]#0(바로위)~7(좌상)
dy = [-1,-1,0,1,1,1,0,-1]
# [r,c,m,s,d]
def decideDR4(dboard,ny,nx,d):
    curD = dboard[ny][nx]
    if curD == -1:
        curD = d#맨처음이면 걍 자기자신이 방향.
    elif curD == 8:
        return dboard
    elif 0<=curD<=7:
        if curD %2 != d%2:#이전 방향이랑 현재방향이랑 짝홀 다르면 False
            curD = 8
    dboard[ny][nx] = curD
    return dboard
# def divideBalls(board,m_s,pv):
#     # newFball = []
#     # for i in range(M):
#     #     fb = fball[i]
#     #     if tuple([fb[0]-1,fb[1]-1]) in pv:
#     #         cnt = board[fb[0]-1][fb[1]-1]
#     #         fb[2] //= 5
#     #         fb[3] //= cnt
#     #         fb[4] = newdr(board,tuple([fb[0]-1,fb[1]-1]))#이 위치에 있는 애들 방향 생각해서 
#     #         if fb[3] == 0:
#     #             continue
#     #     newFball.append(fb)
#     # return newFball
#     tmp = []
#     newFball = []
#     for p in pv:#pv는 0부터 시작하는 인덱스들로 구성
#         cnt = board[p[0]][p[1]]#해당 위치에 중첩된 볼 개수
#         #질량/5,속도/cnt해줘야됨 각 fb에 대해서..
#         m,s=m_s[p[0]][p[1]]
#         m //= 5
#         s //= cnt
        


def move(fball_i,board=None,m_s=None,dboard=None,pv=None):#맨 처음엔 보드도 피봇도 없음
    #i번쨰 fball원소가 들어오면
    r,c,m,s,d = fball_i
    if not board:#board없으면 weight도 pv도 없음
        board = [[0 for _ in range(N)] for _ in range(N)]#원형큐라고 생각해야됨. 밖으로 떨어지는거없음
        m_s = [[[0,0] for _ in range(N)] for _ in range(N)]
        dboard = [[-1 for _ in range(N)] for _ in range(N)]
        pv = []
    #현위치에서 방향과 속도만큼 이동해서 board에 위치 심기
    ny,nx = ((r-1) + dy[d]*s)%N, ((c-1) + dx[d]*s)%N#r,c는 1부터 시작해서 1빼줘야됨
    # if board[ny][nx] >0:
    if (ny,nx) not in pv:
        pv.append((ny,nx))#두개이상이 만나는 지점으로,나중에 처리해줘야하는 부분.
    
    board[ny][nx] += 1#중첩 볼 개수
    m_s[ny][nx]  = [m_s[ny][nx][0] + m,m_s[ny][nx][1] + s]#질량과 속도 더해줘서 나중에 나눠줄거임
    
    dboard = decideDR4(dboard,ny,nx,d)
    
    return board,m_s,dboard,pv

def setNewFireBall(board,m_s,dboard,pv):
    newFball = []
    for p in pv:
        y,x=p
        cnt = board[y][x]  
        
        if cnt > 1:
            if dboard[y][x] == 8 :#방향중한개라도 짝홀 틀리면 8임 아니면 9임
                dr4=[1,3,5,7]
            elif 0<=dboard[y][x]<=7:
                dr4=[0,2,4,6] 
            for i in range(4):
                nm, ns = m_s[y][x][0]//5,m_s[y][x][1]//cnt
                if nm<=0 or ns<=0: 
                    continue
                newFball.append([y+1,x+1,nm, ns,dr4[i]])
        else:
            newFball.append([y+1,x+1,m_s[y][x][0],m_s[y][x][1],dboard[y][x]])
    return newFball

def totalM(fball):
    ans = 0
    for fb in fball:
        ans += fb[2]
    return ans




import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

T = int(input())
# print(T,type(T))
for _ in range(T):
    N,M,K = list(map(int,input().split()))
    #NxN격자에 fb M개 발사.
    #fball=[[r,c,m,s,d]*M]=>i번 파이어볼의 위치는 (ri, ci), 
    # 질량은 mi이고, 방향은 di, 속력은 si이다. 
    # 위치 (r, c)는 r행 c열을 의미한다.

    fball = [list(map(int,input().split())) for _ in range(M)]
    #두 공이 만나면 4개로 찢어지는데
    #합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 
    # 방향은 0, 2, 4, 6이 되고, 
    # 그렇지 않으면 1, 3, 5, 7이 된다.
    # 질랼은 합/5
    # 속력은 합/합쳐진개수
    #질량 0되면 소멸
    #k번 이동하고 남은 질량 합 리턴
    while fball and K>0:#질량이 0된 fball은 리스트에서 빠지니까 K번보다 먼저 없어지면 종료
        
        for i in range(len(fball)):
            if i == 0:
                board,m_s,dboard,pv = move(fball[i])# 이전방향이랑 다르면 8을 넣고 같으면 자기자신을 넣는다.
            else:
                board,m_s,dboard,pv = move(fball[i],board,m_s,dboard,pv)
        fball = setNewFireBall(board,m_s,dboard,pv)
        # fball = divideBalls(board,m_s,pv)#fball에 있는애들 move 다 끝나고 새로운 fball로 정리.
        K-=1
    print(totalM(fball))
#output:8,8,0,9 