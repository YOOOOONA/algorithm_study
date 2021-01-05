
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