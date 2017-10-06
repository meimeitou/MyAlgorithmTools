from functools import reduce
s, a, b, c = [x for x in map(int, input().split())]

ls = sorted([a, b, c], reverse=True)


def factorial(n):
    return reduce(lambda x, y: x * y, [1] + [x for x in range(1, n + 1)])


def Ce(n, m):
    return factorial(n) // (factorial(m) * factorial(n - m))


# print(Ce(3,1))
ls2 = []
ls3 = []
flag = False
ls2.append(Ce(s, ls[0]))
ls3.append(Ce(s, ls[0]))
if s - ls[0] > 0:
    left = s - ls[0]
    if left >= ls[1]:
        ls2.append(Ce(left, ls[1]))
        if left - ls[1] == ls[2]:
            ls2.append(1)
        else:
            ls2.append(Ce(ls[2], left - ls[1]))
    else:  # 剩下不多 不够放ls[1]
        flag = True
        ls2.append(Ce(ls[1], left) + Ce(s - left, ls[1] - left))
        ls2.append(Ce(s, ls[2]))
        ls3.append(Ce(ls[2], left) + Ce(s - left, ls[2] - left))
        ls3.append(Ce(s, ls[1]))
else:
    for i in ls[1:]:
        ls2.append(Ce(s, i))
if flag:
    res = reduce(lambda x, y: x * y, ls3) % 1000000007
else:
    res = []
print(reduce(lambda x, y: x * y, ls2) % 1000000007 + res)
