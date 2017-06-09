#try:
#    f = open('file/file.xxx', 'r')
#    f.read()
#finally:
#    if f:
#        f.close()

#with open('file/file.xxx', 'r') as f:
#    f.read()

#�κζ���ֻҪʵ���������Ĺ����Ϳ�����with���
#ʵ�������Ĺ�����ͨ��__enter__��__exit__����������ʵ�ֵ�

#class Query(object):
    
#    def __init__(self, name):
#        self.name = name
#    def __enter__(self):
#        print('Begin')
#        return self
#    def __exit__(self, exc_type, exc_value, traceback):
#        if exc_type:
#            print('Error')
#        else:
#            print('End')
#    def query(self):
#        print('Query info about %s...' % self.name)

##��д__enter__��__exit__��Ȼ�ܷ��������Python�ı�׼��contextlib�ṩ�˼򵥵�д��
#from contextlib import contextmanager
#class QueryNew(object):
#    def __init__(self, name):
#        self.name = name
#    def query(self):
#        print('Query info about %s.' % self.name)

#@contextmanager
#def create_query(name):
#    print('Begin')
#    q = QueryNew(name)
#    yield q
#    print('End')

#with Query('bob') as q:
#    q.query()

#with create_query('tom') as q2:
#    q2.query()


#�ܶ�ʱ������ϣ����ĳ�δ���ִ��ǰ���Զ�ִ���ض����룬Ҳ������@contextmanagerʵ��
from contextlib import contextmanager
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('<%s>' % name)

with tag('h1'):
    print('what')
    print('happened ?')

#����ִ��˳��
# 1. with�������ִ��yield֮ǰ�����
# 2. yield���û�ִ��with����ڵ��������
# 3. ���ִ��yield֮������
# ��ˣ�@contextmanager������ͨ����дgenerator���������Ĺ���