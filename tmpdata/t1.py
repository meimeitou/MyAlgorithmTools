minNum, maxNum = (x for x in map(int, input().split()))
fishNum = input()
fishList = [x for x in map(int, input().split())]

fishList.sort()
fishList = set(fishList)
safty = set(range(minNum, maxNum + 1))


def getDanger(ins):
    left = set(range(ins * 2, ins * 10 + 1))
    rin = ins // 10
    if rin == 0:
        rin = 0
    right = set(range(rin, ins // 2))
    return left | right


for i in fishList:
    safty = safty - getDanger(i)
print(len(safty))


# 2 22 22 2 2 2 2 2 22 22 2 2 2 22 2 2 2 22 22 2 22 2 2 2 22 2 22 22 2 2 2 22 2 2 2 2 22 222 22 2 2 222 22 2 2 22 22 222
