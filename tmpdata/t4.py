from functools import reduce
import operator
import myfuctiontools
from collections import deque
#num=int(input())
ls=deque([x for x in map(int,input().split())])


def get_sum(ls):
    tmps=0
    for i in ls:
        tmps+=i
    return tmps


def check(inls):
    if len(inls)<=1:
        return True
    else:
        tps=set([])
        for x  in zip(inls[:],inls[1:]):
            tps.add(x[0]-x[1])
        return True if len(tps)==1 and (1 in tps or -1 in tps) else False


print(myfuctiontools.splitListByFunction(ls,check))