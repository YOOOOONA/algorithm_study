# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:01:26 2019

@author: 융
"""

#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
mem=[0 for _ in range(81)]
class Solution:
    
    def solution(self, n):
        if(n==0):
            answer=0
            return answer
        elif(n==1 or n==2):
            return 1
        elif(n>2):
            m=n
            if(mem[m]==0):
                answer=Solution.solution(self,n-1)+Solution.solution(self,n-2)
                mem[m]=answer
            else:
                return mem[m]
            return answer
ans=Solution()
print(ans.solution(3))
