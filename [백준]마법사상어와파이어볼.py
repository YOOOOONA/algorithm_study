dx = [0,1,1,1,0,-1,-1,-1]#0(바로위)~7(좌상)
dy = [-1,-1,0,1,1,1,0,-1]

def divideBalls(board,pv):
    # newFball = []
    # for i in range(M):
    #     fb = fball[i]
    #     if tuple([fb[0]-1,fb[1]-1]) in pv:
    #         cnt = boardfb[0]-1][fb[1]-1]
    #         fb[2] //= 5
    #         fb[3] //= cnt
    #         fb[4] = newdr(board,tuple([fb[0]-1,fb[1]-1]))#이 위치에 있는 애들 방향 생각해서 
    #         if fb[3] == 0:
    #             continue
    #     newFball.append(fb)
    # return newFball
    tmp = []
    for p in pv:#pv는 0부터 시작하는 인덱스들로 구성
        cnt = board[p[0]][p[1]]#해당 위치에 중첩된 볼 개수
        #질량/5,속도/cnt해줘야됨 각 fb에 대해서..
        newFball = []
        
        m=0
        curD = -1
        flag = True
        for i in range(M):
            fb=fball[i]
            if (tuple([fb[0]-1,fb[1]-1]) == p):
                m+=fb[2]
                if curD == -1:
                    curD = fb[4]#맨처음이면 걍 자기자신이 방향.
                else:
                    if curD != fb[4]:#이전 방향이랑 현재방향이랑 다르면 False
                        flag = False
                        # break#바로 방향결정됨 근데 질량 다 받아야되니까 break안함.
            if flag:
                dr4 = [0,2,4,6]
            else:
                dr4 = [1,3,5,7]
            
            if fb[2] == 0:#질량이 0되면 없애버려
                continue
            for j in range(4):
                dd = dr4[i]
                ny = fb[0] + dx[dd]
                nx = fb[1] + dx[dd]
                newFball.append([ny+1,nx+1,m,s,d])
def move(fball_i,board=None,pv=None):#맨 처음엔 보드도 피봇도 없음
    #i번쨰 fball원소가 들어오면
    r,c,m,s,d = *fball_i
    if not board:
        board = [[0 for _ in range(N)] for _ in range(N)]#원형큐라고 생각해야됨. 밖으로 떨어지는거없음
    if not pv:
        pv = []
    #현위치에서 방향과 속도만큼 이동해서 board에 위치 심기
    ny,nx = (r-1) + dy[d]*s, (c-1) + dx[d]*s#r,c는 1부터 시작해서 1빼줘야됨
    if board[ny%N][nx%N] >0:
        if (ny%N,nx%N) not in pv:
            pv.append((ny%N,nx%N))#두개이상이 만나는 지점으로,나중에 처리해줘야하는 부분.
    board[ny%N][nx%N] += 1
    fball_i = [ny+1,nx+1,m,s,d]
    return fball_i,board,pv

T = int(input())
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
                fball_i,board,pv = move(fball[i])
            else:
                fball_i,board,pv = move(fball[i],board,pv)

        fball = divideBalls(board,pv)#fball에 있는애들 move 다 끝나고 새로운 fball로 정리.
        K-=1
#output:8,8,0,9 