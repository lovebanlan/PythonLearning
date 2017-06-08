#
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

#�б�����ͷβ����/ɾ��
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

#defaultdict ����key������ʱ����Ĭ��ֵ�������dict��ȫһ��
from collections import defaultdict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

#dict��Key������ģ�����ʱ�޷�ȷ��key��˳��OrderedDict��key�ᰴ�ղ����˳������
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

#�Ƚ��ȳ��Ķ��У���������������ʱ����ɾ��������ӵ�key��
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

#counter �򵥵ļ�����, ����ͳ���ַ����ֵĴ���
from collections import Counter
c = Counter()
for ch in 'programming is so much fun':
    c[ch] = c[ch] + 1

print(c)