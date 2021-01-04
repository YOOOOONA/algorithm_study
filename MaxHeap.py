# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 12:22:29 2020

@author: 융
"""
#max_heap
class Heap:
    def __init__(self,data):
        self.heap_array = list()
        self.heap_array.append(None)#인덱스 1번부터 들어가려고
        self.heap_array.append(data)
        
    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx // 2
        #추가된자리의 원소가 그 부모의 원소보다 크면 부모자리로 올려줘야지
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False
    def insert(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1
        
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx],self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True
    
    def move_down(self, popped_idx):
        left_child_idx = popped_idx * 2
        right_child_idx = popped_idx * 2 + 1
        if left_child_idx >= len(self.heap_array):
            return False
        elif right_child_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_idx]:
                return True
            
    def pop(self):#보통 힙에서의 삭제는 루트노드 삭제가 일반적
        if len(self.heap_array) <= 1:
            return None
        returned_data = self.heap_array[1]
        return returned_data
        
        