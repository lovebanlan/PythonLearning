#
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

#列表，可以头尾增加/删除
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

#defaultdict 除了key不存在时返回默认值，其余和dict完全一致
from collections import defaultdict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

#dict的Key是无序的，迭代时无法确定key的顺序，OrderedDict的key会按照插入的顺序排序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

#先进先出的队列，当容量超出限制时，先删除最早添加的key：
from collections import OrderedDict
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove: ', last)
        if containsKey:
            del self[key]
            print('set: ', (key, value))
        else:
            print('add: ', (key, value))
        OrderedDict.__setitem__(self, key, value)

lod = LastUpdateOrderedDict(4)
for i in range(10):
    lod[i] = i
print(lod)

#counter 简单的计数器, 例如统计字符出现的次数
from collections import Counter
c = Counter()
for ch in 'programming is so much fun':
    c[ch] = c[ch] + 1

print(c)