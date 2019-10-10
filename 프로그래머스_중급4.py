# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:39:16 2019

@author: 융
"""
#"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2개만 제대로된 스킬트리임
'''
def solution(skill, skill_trees):#skill=선생스킬 순서, skill_trees=스킬트리배열
    answer = 0#가능한 트리개수 출력
    조건에 해당하는 문자가 하나도 없을 떄: 가능
    선행문자가 없는데 후행문자가 나타나면:불가능
    for t in range(skill_trees):
        for i in t:
            for j in skill:
                if j!=i and
    return answer
'''
def solution(skill, skill_trees): 
    answer = 0 
    for ss in skill_trees: 
        skill_list = list(skill) #pop으로 뽑으려고 리스트로 만
        for s in ss: #트리에있는거 하나 중 알파벳한개를 s로받음
            if s in skill: #트리의 알파벳이 스킬에있으면
                if s != skill_list.pop(0): #트리의 알파벳이 스킬의 pop값이 아니면
                    print(ss)
                    break 
        else: answer += 1 #만약 위에꺼 다 아니면~
    print(answer)
    return answer

solution("CBD"	,["BACDE", "CBADF", "AECB", "BDA"])