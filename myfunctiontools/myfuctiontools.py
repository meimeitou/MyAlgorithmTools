'''
splitListByFunction():
如果分组满足func 则分为一组

splitListByNum（）： 按照指定值（每段分组个数）将数组分段

findMax（） 递归二分查找数组中的最大值

Ce（）  返回组合数
'''

# 使用特定条件分割数组  p判断子串是否满足一定条件
from collections import *
from functools import reduce

def splitListByFunction(inls, func):
    ''' 满足func条件的分组
       tmp1 为临时分组变量
       tmp2 为分组集合
    '''
    ls = deque(inls)
    tmp1 = []
    tmp2 = []
    while len(ls) > 0:
        tmp1.append(ls.popleft())
        if not func(tmp1):  # 向tmp1中持续输入值，知道不满足func条件 则将已经添加的值加入到tmp2中
            ls.appendleft(tmp1[-1])
            tmp1.pop(-1)
            tmp2.append(tmp1)
            tmp1 = []
    if len(tmp1) > 0:
        tmp2.append(tmp1)
    return tmp2
# 使用特定值分割数组


def splitListByValue(inls, val):
    pass


def splitListByNum(ins, val):
    '''
    按个数将数组分组  剩下的形成一个分组
    :param ins:
    :param val:
    :return:
    '''
    ls = [x for x in zip(*([iter(ins)] * val))]
    left = len(ins) % val
    if left:
        ls += [tuple(ins[-left:])]
    return ls
# 递归查找数组中的最大值


def findMax(ins, left, right):
    if right - left == 0:
        return ins[left]
    if right - left == 1:
        return max(ins[left], ins[right])
    sp = left + (right - left) // 2
    return max(findMax(ins, left, sp), findMax(ins, sp + 1, right))

# 阶乘 n!
def factorial(n):
    return reduce(lambda x, y: x * y, [1] + [x for x in range(1, n + 1)])

# C(n,k)
def Ce(n, m):
    return factorial(n) // (factorial(m) * factorial(n - m))


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 10, 2, 4, 5, 6, 7]
    print(splitListByNum(a, 5))
    print(findMax(a, 0, len(a) - 1))
