import itertools
def n(z,x):
    re=0
    if z<0:
        re=abs(z)//x
        return re*(-1)
    else:
        re=z//x
        return re

def y(q,dd,y):
    res=a[0]
    for i in range(0,len(dd)):
        if dd[i]=='0':
            res+=a[i+1]
        elif dd[i]=='1':
            res-=a[i+1]
        elif dd[i]=='2':
            res*=a[i+1]
        elif dd[i]=='3':
            res=n(res,a[i+1])
    q.append(res)

N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
yy=[]
for i in range(0,4):
    for j in range(0,b[i]):
        yy.append(str(i))
yy=list(map(''.join,itertools.permutations(yy,len(yy))))
c=[]
ee=set(yy)
yy=list(ee)
for i in range(0,len(yy)):
    y(c,yy[i],a)
print(max(c))
print(min(c))