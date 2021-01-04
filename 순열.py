<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:21:52 2020

@author: 융
"""
def recur(l1,l2,arr):
    arr.append(l1)
    for i,x in enumerate(l2):
        recur(l1+[x],l2[i+1:],arr)
        
def comb(l):
    result = []
    recur([],l,result)
    return result[1:]
    
def perm(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in perm(arr[:i]+arr[i+1:],r-1):
                yield [arr[i]]+next
            





#이거 중복 순열
def permutation(arr,r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    
    def generate(chosen,used):
        if len(chosen) == r:
            print(chosen)
            return
        for i in range(len(arr)):
            chosen.append(arr[i])
            used[i] = 1
            generate(chosen,used)
            chosen.pop()
            used[i] = 0
            
    generate([],used)





def perm2(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in perm2(arr[:i]+arr[i+1:],r-1):
                yield [arr[i]] + next
for i in perm2([1,2,3,4],2):
    print(i)
            


'''  
#permutation([1,2,3,4],2)
    
#단순 순열
def permutations_2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations_2(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next
print(*permutations_2([1,3,5,7,8],3))
print(len([*permutations_2([1,3,5,7,8],3)]))
#for i in permutations_2([1,2,3,4],0):
#    print(i, end=" ")
'''


#단순 조합           
def recur(l1,l2,arr):
    arr.append(l1)
    for i,x in enumerate(l2):
        recur(l1+[x],l2[i+1:],arr)
def comb(l):
    result = []
    recur([],l,result)
=======
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:21:52 2020

@author: 융
"""
def recur(l1,l2,arr):
    arr.append(l1)
    for i,x in enumerate(l2):
        recur(l1+[x],l2[i+1:],arr)
        
def comb(l):
    result = []
    recur([],l,result)
    return result[1:]
    
def perm(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in perm(arr[:i]+arr[i+1:],r-1):
                yield [arr[i]]+next
            





#이거 중복 순열
def permutation(arr,r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    
    def generate(chosen,used):
        if len(chosen) == r:
            print(chosen)
            return
        for i in range(len(arr)):
            chosen.append(arr[i])
            used[i] = 1
            generate(chosen,used)
            chosen.pop()
            used[i] = 0
            
    generate([],used)





def perm2(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in perm2(arr[:i]+arr[i+1:],r-1):
                yield [arr[i]] + next
for i in perm2([1,2,3,4],2):
    print(i)
            


'''  
#permutation([1,2,3,4],2)
    
#단순 순열
def permutations_2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations_2(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next
print(*permutations_2([1,3,5,7,8],3))
print(len([*permutations_2([1,3,5,7,8],3)]))
#for i in permutations_2([1,2,3,4],0):
#    print(i, end=" ")
'''


#단순 조합           
def recur(l1,l2,arr):
    arr.append(l1)
    for i,x in enumerate(l2):
        recur(l1+[x],l2[i+1:],arr)
def comb(l):
    result = []
    recur([],l,result)
>>>>>>> 8912e574d4896c30f8fbe673f8374d993e5ac05e
    return result