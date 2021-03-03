def solution(triangle):
    answer = 0
    
    for i in range(1,len(triangle)):
        for j in range(i+1):
            origin = triangle[i][j]
            for k in range(-1,1):
                if j+k>=0:
                    try:
                        triangle[i][j] = max(triangle[i][j],origin+triangle[i-1][j+k])
                    except:
                        continue
    answer = max(triangle[-1])
    return answer#거쳐간 숫자의 합이 가장 큰 경우