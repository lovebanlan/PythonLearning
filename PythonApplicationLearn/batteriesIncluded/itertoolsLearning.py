#python�ăȽ�ģ��itertools�ṩ�˻ᳪ���õ����ڲ�����������ĺ���
import itertools

#���ߵ�����Ȼ��
#natuals = itertools.count()
#for n in natuals:
#    print(n)

#cycle() ��ɴ����һ�����������ظ���ȥ
#cs = itertools.cycle('ABC')
#for c in cs:
#    print(c)

#repeat()�����һ��Ԫ�������ظ���ȥ������ṩ�ڶ��������Ϳ����޶��ظ�����
#ns = itertools.repeat('A', 10)
#for n in ns:
#    print(n)

#����������Ȼ�������޵�����ȥ������ͨ�����ǻ�ͨ��takewhile()�Ⱥ���������������ȡ��һ�����޵�����
naturals = itertools.count(1)
ns = itertools.takewhile(lambda x : x <= 10, naturals)
ns = list(ns)
for n in ns:
    print(n)

#chain()���԰�һ������������������γ�һ������ĵ�����
for c in itertools.chain('abc', 'xyz'):
    print(c)

#groupby()���԰ѵ�������  ����  ���ظ�Ԫ������������һ��
for key, group in itertools.groupby('aaaBBBAAccAAaa'):
    print(key, list(group))


#itertoolsģ���ṩ��ȫ�����Ǵ���������ܵĺ��������ǵķ���ֵ����list������
#Iterator��ֻ����forѭ��������ʱ�����������