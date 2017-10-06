from itertools import *
num=int(input())

ls=[]
for i in range(num):
    ls.append(input())

def yeildnext(init,maxnum):
    tmp=init
    n=2
    while True:
        yield tmp*n
        if tmp*n>maxnum:break
        n+=1

def getRes(ls):
    res=[]
    for ns in ls:
        maxnu=int(''.join(sorted(ns,reverse=True)))
        for i in yeildnext(int(ns),maxnu):
            if set(ns)==set(str(i)):
                res.append('Possible')
                break
        else:
            res.append('Impossible')
    return res
for i in getRes(ls):
    print(i)