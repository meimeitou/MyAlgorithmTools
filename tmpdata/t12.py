__author__ = 'yinqiwei'
from collections import deque
n,x=[x for x in map(int,input().split())]
lst=[x for x in map(int,input().split())]

lst=deque(lst)
i=0
r=0
while True:
    lst[x-1]-=1
    i+=1
    if lst[x-1]==0:
        break
    lst.rotate(1)
    r+=1
lst.rotate(1)
r+=1
for _ in range(len(lst)-1):
    lst[x-1]-=1
    i+=1
    lst.rotate(1)
    r+=1
lst[x-1]=i
lst.rotate(-r)
print(' '.join(map(str,lst)))