def solution(info, query):
    #info=개발언어 직군 경력 소울푸드 점수
    #query=[조건] X
    #'-' 표시는 해당 조건을 고려하지 않겠다
    answer = []
    infoLi = list(map(lambda x:list(x.split()),info))
    # print(infoLi)
    tmp = list(map(lambda x:list(x.split(" ")),query))
    queryLi = [[x[0],x[2],x[4],x[6],x[7]] for x in tmp]
    # print(queryLi)
    for q in queryLi:
        
        for ifm in infoLi:
            want = []
            flag=True
            for j in range(4):
                if q[j] not in ifm: flag = False;break
            
            if flag and ifm[4]>=q[4]:#모든 쿼리 충족됐을떄
                want.append(ifm)
            answer.append(len(want))

    
    return answer#각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 
print(solution(["java backend junior pizza 150",
          "python frontend senior chicken 210",
          "python frontend senior chicken 150",
          "cpp backend senior pizza 260",
          "java backend junior chicken 80",
          "python backend senior chicken 50"],   
         
         ["java and backend and junior and pizza 100",
          "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250",
          "- and backend and senior and - 150",
          "- and - and - and chicken 100",
          "- and - and - and - 150"]))
#   output:[1,1,1,1,2,4]