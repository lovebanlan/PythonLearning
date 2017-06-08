from multiprocessing import Process, Pool
import os, time, random

#def run_proc(name):
#     print('Run child process %s (%s)' % (name, os.getpid()))

#if __name__ == '__main__':
#   print('parent process %s.' % os.getpid())
#   p = Process(target=run_proc, args=('test', ))
#   print('child process will start.')
#   p.start()
#   p.join()
#   print('child process end.')


#def long_time_task(name):
#    print('Run task %s (%s).' % (name, os.getpid()))
#    start = time.time()
  
#    time.sleep(random.uniform(0,1) * 3)
#    end = time.time()
#    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

#if __name__ == '__main__':
#    print('Parent process %s.' % os.getpid())
#    p = Pool()
#    for i in range(5):
#        p.apply_async(long_time_task, args=(i, ))
#    print('Waitting for all subprocess done...')
#    p.close()
#    p.join()
#    print('All subprocess done.')


#import subprocess
#print('$ nslookup www.python.org')
#r = subprocess.call(['nslookup', 'www.python.org'])
#print('Exit code:', r)


from multiprocessing import Process, Queue
import os, time, random

def write(queue):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s in queue...' % value)
        queue.put(value)
        time.sleep(random.random())
def read(queue):
    print('Process to read: %s' % os.getpid())
    while True:
        value = queue.get(True)
        print('Get %s from queue...' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    
    pw.start();
    pr.start()
    pw.join()

    pr.terminate()