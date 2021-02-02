from itertools import combinations

def solution(orders,course):
    orders = [sorted(x) for x in orders]
    newD = []
    for c in course:        
        d=dict()
        maxcnt = 0
        for w in orders:            
            for x in combinations(w,c):
                if x not in d:d[x]=1 
                else: 
                    d[x]+=1 
                    maxcnt=max(maxcnt,d[x])
        
        # print(d)
        for a in d:
            if d[a]>=2 and maxcnt==d[a]:
                newD.append(''.join(a)) 
        
    return sorted(newD)