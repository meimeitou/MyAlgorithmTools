s=int(input())
d,v=divmod(s,3)
#print(d,v)
if v==0:
    re=''
    for i in range(d):
        re+='21'
    print(int(re))
else:#
    re=''
    for i in range(d):
        re+='12'
    if v==2:
        re=str(v)+re
    else:
        re+=str(v)
    print(int(re))