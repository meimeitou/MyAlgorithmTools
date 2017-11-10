A=[['1','2','3','4'],['a','b','c','d','e'],['@','#','$']]

import itertools
from functools import reduce
def mul(A,B):
    re=[]
    for i in A:
        for j in B:
            re.append(i+j)
    return re
print([x for x in reduce(mul,A)])
