# 1.벨트가 한 칸 회전한다.
# 2.가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
#     1.로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 3.올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
# 4.내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
# 종료되었을 때 몇 번째 단계가 진행 중이었는지 구해보자. 가장 처음 수행되는 단계는 1번째 단계이다.
import sys

sys.stdin = open(".\\input.txt")
input = sys.stdin.readline

from collections import deque
def move(bot):
    global Aq
    #컨베이어가 움직였을 때, 로봇이 오른쪽으로 움직일수있는애는 움직이기
    botTemp = [0 for _ in range(len(bot))]
    # for i in range(len(bot)-1,-1,-1):
    i=len(bot)-1
    while i>0:
        if bot[i-1] == 1:#이동할 로봇이 있는 상황
            if Aq[i] != 0:#다음칸이 0이 아니면 그 칸으로 이동
                botTemp[i] = 1
                Aq[i] -= 1
            else:
                botTemp[i-1] = 1
                i -= 1#제자리에 로봇두기=>이동안해서 Aq 안줄어듦                
        i-=1
    return botTemp
            
for _ in range(4):
    N,K = map(int,input().split())
    Alist = list(map(int,input().split()))
    #deque.rotate쓰거나 그냥 que쓰거나

    Aq = deque(Alist)
    bot = deque(0 for _ in range(N))
    cnt = 0
    while(Aq.count(0) < K):
        #1
        Aq.rotate(1)#회전하면서
        bot = move(bot)#이동하고
        # print('before',Aq)
        if Aq[0]!=0:Aq[0] -= 1#위로 올리면 하나 감소
        if Aq[N]!=0:Aq[N] -= 1#아래로 내려짐 당한 애 하나 감소
        
        if Aq[0]!=0 and bot[0]==0:#올려진후에도 0이 아니고 시작점에 쌓인 로봇 없으면 새 로봇 올려야해
            bot[0] = 1
            Aq[0] -= 1#올리면 감소임
        #로봇이 이동해도 1감소
        # print('after',Aq)
        cnt += 1
    print(cnt)
        
        