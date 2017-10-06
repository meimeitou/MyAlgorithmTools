nu = int(input())

ls = []
for i in range(nu):
    ls.append([x for x in map(int, input().split())])

rg = int(input())


def ploy(ls, x):
    return ls[0] * pow(x, 7) + ls[1] * pow(x, 6) + ls[2] * pow(x, 5) +\
        ls[3] * pow(x, 4) + ls[4] * pow(x, 3) + ls[5] * \
        pow(x, 2) + ls[6] * pow(x, 1) + ls[7]


tmp = []
for i in range(nu):
    tmp.append(1)


def nextOne(ls):
    tp = []
    for i, v in enumerate(tmp):
        tp.append([ploy(ls[i], v), i])
    tp.sort(key=lambda x: x[0])
    tmp[tp[0][1]] += 1
    return tp[0][0]


res = 0
for _ in range(rg):
    res = nextOne(ls)

print(res)
