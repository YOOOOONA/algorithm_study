<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:02:26 2020

@author: 융
"""

#1일 이용권 : 1일 이용이 가능하다.
#1달 이용권 : 1달 동안 이용이 가능하다. 1달 이용권은 매달 1일부터 시작한다.
#3달 이용권 : 연속된 3달 동안 이용이 가능하다. 3달 이용권은 매달 1일부터 시작한다.
#       (11월, 12월에도 3달 이용권을 사용할 수 있다 / 다음 해의 이용권만을 구매할 수 있기 때문에 3달 이용권은 11월, 12월, 1윌 이나 12월, 1월, 2월 동안 사용하도록 구매할 수는 없다.)
#1년 이용권 : 1년 동안 이용이 가능하다. 1년 이용권은 매년 1월 1일부터 시작한다.

#연간 월별 이용횟수를 알 때 가장 저렴한 회원권비용 return
import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline

def iterate(monthly_plan,i,months):
    #print('i는',i)
    if 0 not in monthly_plan[i:i+3]:
        months.extend([i,i+1,i+2])
        i += 3#3개 연속 찾으면 3뒤로 가고
    else:
        i += 1#그렇지 않으면 한칸만 뒤로
        
    if i+3<11:
        return iterate(monthly_plan,i,months)
    else:
        #print('months',i,months)
        return months
    
def solution(day, mon, mon3, year,monthly_plan):
    chpstPrice = 1 * year#일단 cheapst는 maximum으로 초기화. 1년치를 끊는게 맥시멈일테니까.
    
    threshold = mon // day + 1#한달 100원, 하루 30원일때 3+1일만 나가면 한달이 이득
    #1일&1월으로 계산한 가격 한번에 구함
    price = 0
    for i in monthly_plan:
        if i < threshold: price += i * day
        else: price += 1 * mon
    chpstPrice = min(price,chpstPrice)
    
    #3달연속인거 구하기
    monthsVote = []
    
    for i in range(10):
        months = []
        a = iterate(monthly_plan,i,months)
        #print('a?',a)
        monthsVote.append(a) if (len(a) > 0 and a not in monthsVote) else None
    print(monthly_plan,'\nmonthsVode',monthsVote)
    
    #세달짜리 금액 + 1달로 할지 1일로 할지 정해야됨
    #1달이 더 싸지는 날짜 구하기
    
    
    for mths in monthsVote:
        tot = len(mths) // 3 * mon3
        for i in range(0,12):
            if i not in mths and monthly_plan[i] != 0:
                if monthly_plan[i] >= threshold:
                    tot += mon
                else:
                    tot += monthly_plan[i] * day
                        
        chpstPrice = min(tot,chpstPrice)
    
    return chpstPrice

if __name__ == '__main__':
    T = int(input())
    for i in range(1,T+1):
        day, mon, mon3, year = map(int,input().split())
        monthly_plan = list(map(int,input().split()))
        print("#%d %d" %(i,solution(day, mon, mon3, year,monthly_plan)))
=======
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:02:26 2020

@author: 융
"""

#1일 이용권 : 1일 이용이 가능하다.
#1달 이용권 : 1달 동안 이용이 가능하다. 1달 이용권은 매달 1일부터 시작한다.
#3달 이용권 : 연속된 3달 동안 이용이 가능하다. 3달 이용권은 매달 1일부터 시작한다.
#       (11월, 12월에도 3달 이용권을 사용할 수 있다 / 다음 해의 이용권만을 구매할 수 있기 때문에 3달 이용권은 11월, 12월, 1윌 이나 12월, 1월, 2월 동안 사용하도록 구매할 수는 없다.)
#1년 이용권 : 1년 동안 이용이 가능하다. 1년 이용권은 매년 1월 1일부터 시작한다.

#연간 월별 이용횟수를 알 때 가장 저렴한 회원권비용 return
import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline

def iterate(monthly_plan,i,months):
    #print('i는',i)
    if 0 not in monthly_plan[i:i+3]:
        months.extend([i,i+1,i+2])
        i += 3#3개 연속 찾으면 3뒤로 가고
    else:
        i += 1#그렇지 않으면 한칸만 뒤로
        
    if i+3<11:
        return iterate(monthly_plan,i,months)
    else:
        #print('months',i,months)
        return months
    
def solution(day, mon, mon3, year,monthly_plan):
    chpstPrice = 1 * year#일단 cheapst는 maximum으로 초기화. 1년치를 끊는게 맥시멈일테니까.
    
    threshold = mon // day + 1#한달 100원, 하루 30원일때 3+1일만 나가면 한달이 이득
    #1일&1월으로 계산한 가격 한번에 구함
    price = 0
    for i in monthly_plan:
        if i < threshold: price += i * day
        else: price += 1 * mon
    chpstPrice = min(price,chpstPrice)
    
    #3달연속인거 구하기
    monthsVote = []
    
    for i in range(10):
        months = []
        a = iterate(monthly_plan,i,months)
        #print('a?',a)
        monthsVote.append(a) if (len(a) > 0 and a not in monthsVote) else None
    print(monthly_plan,'\nmonthsVode',monthsVote)
    
    #세달짜리 금액 + 1달로 할지 1일로 할지 정해야됨
    #1달이 더 싸지는 날짜 구하기
    
    
    for mths in monthsVote:
        tot = len(mths) // 3 * mon3
        for i in range(0,12):
            if i not in mths and monthly_plan[i] != 0:
                if monthly_plan[i] >= threshold:
                    tot += mon
                else:
                    tot += monthly_plan[i] * day
                        
        chpstPrice = min(tot,chpstPrice)
    
    return chpstPrice

if __name__ == '__main__':
    T = int(input())
    for i in range(1,T+1):
        day, mon, mon3, year = map(int,input().split())
        monthly_plan = list(map(int,input().split()))
        print("#%d %d" %(i,solution(day, mon, mon3, year,monthly_plan)))
>>>>>>> 8912e574d4896c30f8fbe673f8374d993e5ac05e
        #break