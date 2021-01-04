<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:37:29 2020

@author: 융
"""

def comb(ans,arr,cnt):
    arr2=arr.copy()
    
    print(arr2,cnt)
    if cnt==0:
        print(arr2,cnt)
        return ans
    elif cnt==1:
        print(arr2,cnt)
        for i in range(len(arr)):
            a = arr[i]
            if a not in ans:
                ans.append(a)
    elif cnt==2:
        print(arr2,cnt)
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                comb(ans,arr2,1)
                a = arr[i]+arr[j]
                if a not in ans:
                    ans.append(a)
    else:
        
        print(arr2,cnt)
        for i in range(len(arr)):
            arr2=arr.copy()
            arr2.remove(arr[i])
            print('왜',i,arr2)
            ans.extend(comb(ans,arr2,cnt-1))
            ans=list(set(ans))
        print('이',arr2,cnt)    
    return ans
ans = []
print(comb(ans,[1,2,3,4],4))                
=======
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:37:29 2020

@author: 융
"""

def comb(ans,arr,cnt):
    arr2=arr.copy()
    
    print(arr2,cnt)
    if cnt==0:
        print(arr2,cnt)
        return ans
    elif cnt==1:
        print(arr2,cnt)
        for i in range(len(arr)):
            a = arr[i]
            if a not in ans:
                ans.append(a)
    elif cnt==2:
        print(arr2,cnt)
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                comb(ans,arr2,1)
                a = arr[i]+arr[j]
                if a not in ans:
                    ans.append(a)
    else:
        
        print(arr2,cnt)
        for i in range(len(arr)):
            arr2=arr.copy()
            arr2.remove(arr[i])
            print('왜',i,arr2)
            ans.extend(comb(ans,arr2,cnt-1))
            ans=list(set(ans))
        print('이',arr2,cnt)    
    return ans
ans = []
print(comb(ans,[1,2,3,4],4))                
>>>>>>> 8912e574d4896c30f8fbe673f8374d993e5ac05e
