from itertools import permutations

def isMatch(user_set, banned_set):
    for i in range(len(user_set)):
        if len(user_set[i])!=len(banned_set[i]):
            return False
        for j in range(len(user_set[i])):
            if banned_set[i][j]=='*':
                continue
            if user_set[i][j]!=banned_set[i][j]:
                return False
    return True
    
def solution(user_id, banned_id):
    ans=[]
    for com_set in permutations(user_id, len(banned_id)):#이걸 set으로 중복검사를 하는게 더 오래걸림.
        
        if isMatch(com_set, banned_id):
            print(1,com_set,type(com_set))#tuple
            com_set = {*com_set} # 중복 제거아니고,이 형태(set)로 가야되는거
            print(2,com_set,type(com_set))#set
            if com_set not in ans:
                ans.append(com_set)
    return len(ans)