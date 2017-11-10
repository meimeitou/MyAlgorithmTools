__author__ = 'yinqiwei'
n,m=[x for x in map(int,input().split())]
ls=[]
for _ in range(n):
    ls.append(input())

def find(ls):
    e=(0,0)
    s=(0,0)
    o=(0,0)
    for i,row in enumerate(ls):
        for j,col in enumerate(row):
            if col=='E':
                e=(i,j)
            elif col == 'S':
                s=(i,j)
            elif col=='0':
                o=(i,j)
    return e,o,s
E,O,S=find(ls)
mint=abs(O[0]-E[0])+abs(O[1]-E[1])
mins=abs(O[0]-S[0])+abs(O[1]-S[1])
print(11)