# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:56:03 2020

@author: 융
"""
'''
def solution(s):#1~1000,알파벳소문자
    answer = 1000
    
    for i in range(1 , len(s) // 2 + 1):#자르는 단위를 늘려가며 압축도 비교#i=1
        cnt = 1#2
        stWord = s[:i]
        #for j in range(0,len(s),i):#j=0+1+1
        j = 0
        while j < len(s):
            if s[j:j+i] == s[j+i:j+i+i]:#b
                cnt += 1
                now = j+i
                print(now,j,i)
                j = now
            else:
                if j == 0:
                    break
                else:#앞 단어랑 같진 않지만 그 단어가 맨 첫단어는 아닐때
                    if cnt == 1: cnt = ''
                    word = word + str(cnt) + s[j:j+i]#2a
                    cnt = 1
                    now = j+i
                    j = now
                    print(now,j,i)
                #j += 1
        print('now',now)#2
        word = word + s[now:]
        answer = min(answer,len(word))
        print(word,answer)
    print('답',answer)
    return answer #제일 짧은 길이
'''
def solution(s):
    length = []
    result = ""
    
    if len(s) == 1:
        return 1
    
    for cut in range(1, len(s) // 2 + 1): 
        count = 1
        tempStr = s[:cut] 
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i+cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""
    print(min(length))
    return min(length)

solution("aabbaccc")#7
solution("ababcdcdababcdcd")#9
solution("abcabcdede")#8
solution("abcabcabcabcdededededede")#14
solution("xababcdcdababcdcd")#17
solution("bbaabaaaab")#8
solution("zzzbbabbabba")#7   11
solution("xxxxxxxxxxyyy")#5
solution("xyzwxaxyzwxxyzwxb")