#python的內建模块itertools提供了会唱有用的用于操作迭代对象的函数
import itertools

#无线迭代自然数
#natuals = itertools.count()
#for n in natuals:
#    print(n)

#cycle() 会吧传入的一个序列无线重复下去
#cs = itertools.cycle('ABC')
#for c in cs:
#    print(c)

#repeat()负责吧一个元素无线重复下去，如果提供第二个参数就可以限定重复次数
#ns = itertools.repeat('A', 10)
#for n in ns:
#    print(n)

#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件来截取出一个有限的序列
naturals = itertools.count(1)
ns = itertools.takewhile(lambda x : x <= 10, naturals)
ns = list(ns)
for n in ns:
    print(n)

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('abc', 'xyz'):
    print(c)

#groupby()可以把迭代器中  相邻  的重复元素挑出来放在一起
for key, group in itertools.groupby('aaaBBBAAccAAaa'):
    print(key, list(group))


#itertools模块提供的全部都是处理迭代功能的函数，它们的返回值不是list，而是
#Iterator，只有用for循环迭代的时候才真正计算