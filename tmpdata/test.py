from itertools import *
dc={'a': 2, 'c': 4, 'd': 0, 'f':7}
print(dc)

#key 参数用来处理输入数据  cmp参数用来比较大小顺序
print(sorted(dc.items(),key=lambda x:x[1]))
print(dc.get('t',0))

ls=[1,4,6,7,9,3,4,7,2]
#duoxunhuan
for m, n in product('abc', [1, 2]):
    print(m, n)