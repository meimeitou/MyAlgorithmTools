'''
排序算法集合
插入排序
希尔排序
冒泡排序
选择拍序
快速排序
归并排序
--堆排序  heapSort 使用python 内置heapq实现
'''

# 插入排序 递增
import operator


def insertSort(ins, revers=False):
    '''
    :param ins: 输入数组
    :param revers:  是否翻转  正序False  逆序True
    :return:  返回排序数组
    '''
    count = len(ins)
    if not revers:
        op = operator.gt
    else:
        op = operator.lt
    for i in range(1, count):
        tn = ins[i]
        j = i - 1
        while j >= 0:
            if op(ins[j], tn):
                ins[j + 1] = ins[j]
                ins[j] = tn
            j -= 1
    return ins

#希尔排序  ---插入排序中的一种


def shellSort(ins, revers=False):
    '''
    :param ins:
    :param revers:
    :return:
    '''
    gap = len(ins) // 2
    if not revers:
        op = operator.gt
    else:
        op = operator.lt
    while gap > 0:
        for i in range(len(ins)):
            if i + gap == len(ins):
                break
            if op(ins[i], ins[i + gap]):
                ins[i], ins[i + gap] = ins[i + gap], ins[i]
        gap //= 2
    return ins

# 冒泡排序


def bubleSort(ins, revers=False):
    '''

    :param ins:
    :param revers:
    :return:
    '''
    if not revers:
        op = operator.gt
    else:
        op = operator.lt
    curr = len(ins) - 1
    while curr > 0:
        for i in range(curr):
            if op(ins[i + 1], ins[i]):
                ins[i], ins[i + 1] = ins[i + 1], ins[i]
        curr -= 1
    return ins

# 选择排序


def pickSort(ins, revers=False):
    '''
    :param ins:
    :param revers:
    :return:
    '''
    if not revers:
        op = operator.gt
    else:
        op = operator.lt
    sortlen = 0
    inslen = len(ins)
    while sortlen < inslen:
        tmpnum = ins[sortlen]
        index = sortlen
        for i in range(sortlen, inslen):
            if op(ins[i], tmpnum):
                tmpnum = ins[i]
                index = i
        ins[sortlen], ins[index] = ins[index], ins[sortlen]
        sortlen += 1
    return ins

# 快速排序


def quickSort(ins, revers=False):
    '''
    :param ins:
    :param revers:
    :return:
    '''
    if not revers:
        op = operator.ge
    else:
        op = operator.le
    return partation(ins, 0, len(ins) - 1, op)


def partation(ins, left, right, op):
    if left >= right:
        return ins
    key = ins[left]
    low = left
    high = right
    while left < right:
        while left < right and op(ins[right], key):
            right -= 1
        ins[left] = ins[right]
        while left < right and op(key, ins[left]):
            left += 1
        ins[right] = ins[left]
    ins[left] = key
    partation(ins, low, left - 1, op)
    partation(ins, left + 1, high, op)
    return ins

# 归并排序


def mergeSort(ins, revers=False):
    if len(ins) < 2:
        return ins
    if not revers:
        op = operator.ge
    else:
        op = operator.le
    sortgap = len(ins) // 2
    left = mergeSort(ins[:sortgap], revers)
    right = mergeSort(ins[sortgap:], revers)
    return merge(left, right, op)


def merge(left, right, op):
    '''
    合并左右序列
    :param left:
    :param right:
    :return:
    '''
    i, j = 0, 0
    resout = []
    while i < len(left) and j < len(right):
        if op(left[i], right[j]):
            resout.append(left[i])
            i += 1
        else:
            resout.append(right[j])
            j += 1
    if i < len(left):
        resout += left[i:]
    elif j < len(right):
        resout += right[j:]
    return resout


def test(ins, a, b, c):
    ins[0] = 2
    a = 2
    b = 'no change'
    c.clear()
    print(id(a), id(b), id(c))


# 堆排序
import heapq


def heapSort(inls, reverse=False):
    '''
    buidin 中只有小根堆 可以通过插入
    -value值 使小根堆变成大根堆，
    返回值时将负值转化回来即可
    '''
    if reverse:
        inls = [-x for x in inls]
    heapq.heapify(inls)  # 堆初始化
    heap = []
    while inls:
        heap.append(heapq.heappop(inls))
    if reverse:
        inls[:] = [-x for x in heap]
    else:
        inls[:] = heap
    return inls


if __name__ == '__main__':
    ls = [2, 3, -1, -5, 4, -8, 4, 3, 5, 100, 34, 2]

    print(heapSort(ls, True))
    a = 1
    b = 'no change'
    c = set([1, 2])
    print(id(a), id(b), id(c))
    test(ls, a, b, c)
    print(ls)
