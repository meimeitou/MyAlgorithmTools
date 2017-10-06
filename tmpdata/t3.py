# by yinqiwei
import operator
from functools import reduce
nu=int(input())
lst=[]
for i in range(nu):
    lst.append(input())

def get_max(ins):
    if ins==1:
        return 26
    elif ins==0:
        return 0
    else:
        return get_max(ins-1)+reduce(operator.add,range(28-ins))

def get_curr(ins):
    if ins==1:
        return 1
    else:
        return 27-ins

def cal(ins):
    maxnu=get_max(len(ins)-1)
    tm=[]
    subs=ord('a')
    for i in ins:
        tm.append(ord(i)-subs)
        subs+=1
    cunum=get_curr(len(ins))
    sums=0
    #print(tm)
    for i in tm:
        sums+=i*cunum
        cunum-=1
    sums+=1
    #print(maxnu,sums)
    return sums+maxnu
tms=[]
for i in lst:
    tms.append(cal(i))
for i in tms:
    print(i)