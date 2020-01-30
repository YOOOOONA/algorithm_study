def sort_c(li,gagul):
    m=0
    change={'c':0,
           'r':1,
           'o':2,
           'a':3,
           'k':4}
    while(gagul):
        g_p=gagul.pop(0)
        if change[g_p] in li:
            m=max(m,li.index(change[g_p]))
            li[li.index(change[g_p])]=(li[li.index(change[g_p])]+1)%5 #만약 c가 들어오면 리스트에 0자리에 1을 추가하지, 결국 k 까지 들어오면 5가 된 상태. 5로나눈 나머지가 0인거에 c또들어가면 되겠다
        else:
            return -1
    return m+1
 
T=int(input())
for i in range(T):
    gagul=input()
    if gagul.count('c')==gagul.count('r')==gagul.count('o')==gagul.count('a')==gagul.count('k'):
        gagul=list(gagul)
        li=[0 for j in range(gagul.count('c')+2)]
        answer=sort_c(li,gagul)
        print("#%d %d" %(i+1,answer))
    else:
        print("#%d %d" %(i+1,-1))
