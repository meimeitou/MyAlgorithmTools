import sys
from copy import deepcopy
#id  name  up
def checkStr(ins):
    ls=[x for x in ins.split(';')]
    rels=[]
    std=False
    for i in ls:
        id,name,up=i.split(',')
        if not id.isdigit() or not name.isupper() or not up.isdigit():
            return std,rels
        rels.append((int(id),name,int(up)))
    if sorted(rels,key=lambda x : x[0])!=rels:
        return std,[]
    return True,rels

def Res(inls):
    res=[[inls[0][0]]]
    flag=True
    while flag:
        flag=False
        for i,val in enumerate(res):
            find=False
            restmp=deepcopy(res)
            for j in inls:
                if val[-1]==j[-1]:
                    if find==True:
                        restmp.append(res[i]+[j[0]])
                    else:
                        find=True
                        flag=True
                        restmp[i].append(j[0])
            res=restmp
    return res


if __name__=='__main__':
    printlst=[]
    std,strlist=checkStr(input())
    print(std,strlist)
    print(Res(strlist))
    '''
    for st in sys.stdin.readlines():
        std,strlist=checkStr(st)
        if std:
            printlst.append('incorret data')
        else:
            printlst.append(Res(strlist))
    '''