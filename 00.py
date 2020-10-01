def insert_sorting(array, k):
    for i in range(0,len(array)):#0번째 값은 이미 정렬된 것으로 보고 나머지를 삽입대상으로 봄
        key = array[i]
        j=0
        if i == 0 and len(array) == 1:
            return array[0]
        
        elif i == 0 and len(array) > 1:
            if array[1] < key:
                array[0] = array[1]
                array[1] = key
        else:    
            for j in range(i-1,-1,-1):
                if array[j] > key:
                    array[j+1] = array[j]
                else:
                    j=j
                    break
            array[j+1] = key
    print(array)
    return array[k]#정렬 후 k 번째 값 리턴
def solution(array, commands):
    answer = []
    for info in commands:
        i,j,k = info
        print('k:',k)
        answer.append(insert_sorting(array[i-1:j-1+1],k-1))
    return answer
print(solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]]))