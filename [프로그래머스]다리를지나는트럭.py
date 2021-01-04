# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 22:40:24 2020

@author: 융
"""

def solution(bridge_length, weight, truck_weights):
    answer = 1 + bridge_length
    tk_len = len(truck_weights)
    onload = [0,0]#도로위에 있는 무게,맨 첫번째 값의 본래 인덱스
    for i in range(tk_len-1):트럭이 연달아서 오지못할때 예외처리 안
        if i-onload[1] == bridge_length:#현재 지나는 트럭 인덱스랑 도로위의 맨 첫번째 트럭인덱스 차이가 다리길이와 같으면 도로위에서 하나 빼줘야지
            onload[0] -= truck_weights[onload[1]]
            onload[1] += 1
        else:
            if sum(truck_weights[onload[1]:i+1]) <= weight:
                onload[0] += truck_weights[i]
            #else:#이미 도로 무게 넘쳐서 새로 못들어가면 시간만 지나가야지
            #    onload[0] += truck_weights[onload[1]]
        answer += 1
    return answer
        