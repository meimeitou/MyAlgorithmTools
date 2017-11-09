# bin/bash python
import sys


def game():
    num = int(input())
    teamName = {}
    for i in range(num):
        # 积分  净胜球  进球总数
        teamName[input()] = [0, 0, 0]
    numSum = int(num * (num - 1) / 2)
    for _ in range(numSum):
        pk, val = input().split(' ')
        name1, name2 = pk.split('-')
        val1, val2 = val.split(':')
        if int(val1) > int(val2):
            teamName[name1][0] += 3
        elif int(val1) < int(val2):
            teamName[name2][0] += 3
        else:
            teamName[name1][0] += 1
            teamName[name2][0] += 1
        teamName[name1][1] += int(val1)
        teamName[name2][1] += int(val2)
        teamName[name1][2] += (int(val1) - int(val2))
        teamName[name2][2] += (int(val2) - int(val1))
    return teamName


def getNum(teamName):
    teamName = sorted(teamName.items(), key=lambda x: x[1][0], reverse=True)
    teamName = sorted(teamName, key=lambda x: x[1][1], reverse=True)
    teamName = sorted(teamName, key=lambda x: x[1][2], reverse=True)
    teamName = sorted(teamName[:int(len(teamName) / 2)], key=lambda x: x[1][0])
    return teamName


'''
A-B 1:1
A-C 2:2
A-D 1:0
B-C 1:0
B-D 0:3
C-D 0:3
'''


def newGame(team, pks):
    teamName = {}
    for i in team:
        # 积分  净胜球  进球总数
        teamName[i] = [0, 0, 0]
    for vp in pks:
        pk, val = vp.split(' ')
        name1, name2 = pk.split('-')
        val1, val2 = val.split(':')
        if int(val1) > int(val2):
            teamName[name1][0] += 3
        elif int(val1) < int(val2):
            teamName[name2][0] += 3
        else:
            teamName[name1][0] += 1
            teamName[name2][0] += 1
        teamName[name1][1] += int(val1)
        teamName[name2][1] += int(val2)
        teamName[name1][2] += (int(val1) - int(val2))
        teamName[name2][2] += (int(val2) - int(val1))
    return teamName


'''
lins=sys.stdin.readlines()

gets=0
while(gets<len(lins)):
    num = int(lins[gets].strip())
    gets += num+1+int(num*(num-1)/2)

'''
while True:
    tm = getNum(game())
    # print(tm)
    for i in range(len(tm)):
        print(tm[i][0])
