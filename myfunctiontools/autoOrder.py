'''
函数说明：
getNextOrder():  从列表中start位置开始 获取先一个有序的长序列（可以是递增或者递减的）

----shallCandy（）：  分发糖果  基于输入权值输入序列   权值大分发糖果多， 返回最小分发糖果序列

getHeap（） 调整数组为大根堆或者小根堆

TopKHeap  ：返回数据流中 top k个最大值  ，使用系统buildin 结构heapq 小根堆实现，


'''

from operator import lt, gt

# 找到最长递增或者递减数组


def getNextOrder(inls, start=0, auto=False, reverse=False):
    '''
    reverse 参数用来控制递增或者递减
    start控制起始位置
    auto 自动返回递增或递减中较长的一个
    '''
    if len(inls) == 0 or start >= len(inls):
        return [], reverse
    if len(inls) == 1:
        return inls, reverse
    cur = start
    if auto:  # 自动
        or1, or2 = getNextOrder(inls, start), getNextOrder(
            inls, start, reverse=True)
        # print(or1,or2)
        return or1 if len(or1[0]) >= len(or2[0]) else or2
    else:  # 非自动
        if reverse:
            op = lt
        else:
            op = gt
        for i, _ in enumerate(inls[start:], start):
            try:
                if op(inls[i], inls[i + 1]):
                    cur = i + 1
                    break
            except IndexError:
                cur = i + 1
                break
        else:
            cur = len(inls) - 1
        return inls[start:cur], reverse


def shallCandy(inls):
    index = 0
    candy = [0]
    while index < len(inls) - 1:
        # print(index)
        tmp, rev = getNextOrder(inls[index:], auto=True)
        nu = len(tmp)
        startnum = candy[index]
        # print(tmp)
        if rev:  # 逆序
            tmp = [x for x in range(nu, 0, -1)]
            if tmp[0] > startnum:
                candy = candy[:-1] + tmp
            else:
                candy = candy + tmp[1:]
            index = len(candy) - 1
        else:  # 顺序
            tmp = [x for x in range(1, nu + 1)]
            candy = candy[:-1] + tmp
            index = len(candy) - 1
    return candy


def getMiddle(inls1, inls2, k):
    pass

# 调整为大根堆或小根堆


def getHeap(inls, big=True):
    '''
    big  指定小堆或者大堆
    '''
    from operator import lt, gt
    if big:
        op = gt
    else:
        op = lt

    def adjust(ls, size, root, ops):
        left = root * 2
        right = root * 2 + 1
        larger = root
        if left < size and ops(ls[larger], ls[left]):
            larger = left
        if right < size and ops(ls[larger], ls[right]):
            larger = right
        if larger != root:
            ls[larger], ls[root] = ls[root], ls[larger]
            adjust(ls, size, larger, ops)
    heapLen = len(inls)
    for i in range((heapLen - 2) // 2, -1, -1):
        adjust(inls, heapLen, i, op)
    return inls


#使用堆实现topK最大值   (使用小根堆实现)
import heapq


class TopKHeap(object):
    def __init__(self, k, datas=[]):
        self.k = k
        self.data = []
        for i in datas:
            self.push(i)

    def push(self, item):
        if len(self.data) < self.k:  # 小则直接插入数组
            heapq.heappush(self.data, item)
        else:  # 超过后需弹出最小值
            topk_small = self.data[0]
            if topk_small < item:  # 当前插入值大于最小值则删除最小值并插入当前值
                heapq.heapreplace(self.data, item)

    def TopK(self):
        return [x for x in reversed([heapq.heappop(self.data)
                                     for _ in range(len(self.data))])]
# 使用大根堆实现 topk最小值


class TopKMinHeap(object):
    def __init__(self, k):
        self.k = k
        self.data = []

    def push(self, item):
        if len(self.data) < self.k:
            heapq.heappush(self.data, -item)
        else:
            top_large = self.data[0]
            if top_large < -item:
                heapq.heapreplace(self.data, -item)

    def topK(self):
        return [-x for x in reversed([heapq.heappop(self.data) for _ in
                                      range(len(self.data))])]


if __name__ == '__main__':
    # print(getNextOrder([1,4,5,9,3,2],start=3,auto=True,reverse=True))
    # print(shallCandy([1,2,57,3,5,2,6,3]))
    print(getHeap([3, 1, 5, 3, 7, 6], big=False))
    import heapq
    import random
    ls = random.randint(10)
    heapq.heapify(ls)
    tp = TopKHeap(3)
    for i in ls:
        tp.push(i)
    print(tp.TopK())

    mtop = TopKMinHeap(3)
    for i in ls:
        mtop.push(i)
    print(mtop.topK())
