import sys
import math

def prime(n):
    if n%2 == 0:
        return n==2
    if n%3 == 0:
        return n==3
    if n%5 == 0:
        return n==5
    for p in range(7,int(math.sqrt(n))+1,2):
        if n%p == 0:
            return 0
    return 1
def nextOne(ini):
    while True:
        if ini>pow(10,6):return -1
        if prime(ini):
            if str(ini)[::-1]!= str(ini) and prime(int(str(ini)[::-1])):
                return ini
            else:
                ini+=1
        else:
            ini+=1

def yeildPrime(n):
    ini=13
    tmp=13
    while True:
        yield ini
        if ini == -1 : break
        tmp=ini
        ini=nextOne(tmp)


nu=int(input())
tmp=12
for i in range(nu):
    tmp=nextOne(tmp)
    #print(tmp)
    if tmp==-1: break
    tmp+=1
if tmp==-1:
    print(tmp)
else: print(tmp-1)
