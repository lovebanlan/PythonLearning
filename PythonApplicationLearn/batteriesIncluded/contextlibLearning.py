#try:
#    f = open('file/file.xxx', 'r')
#    f.read()
#finally:
#    if f:
#        f.close()

#with open('file/file.xxx', 'r') as f:
#    f.read()

#任何对象只要实现了上下文管理，就可以用with语句
#实现上下文管理是通过__enter__和__exit__这两个方法实现的

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

##编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了简单的写法
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


#很多时候我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
from contextlib import contextmanager
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('<%s>' % name)

with tag('h1'):
    print('what')
    print('happened ?')

#代码执行顺序：
# 1. with语句首先执行yield之前的语句
# 2. yield调用会执行with语句内的所有语句
# 3. 最后执行yield之后的语句
# 因此，@contextmanager让我们通过编写generator来简化上下文管理