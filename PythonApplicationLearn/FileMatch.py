import os

print('input key: ')
fileName = input()
def findFiles(p):
   # print('search: ' + p)
    flist = os.listdir(p)
    for x in flist:
        temp = os.path.join(p, x)
        if os.path.isdir(temp):
            findFiles(temp)
        elif str(x).find(fileName) != -1:
            print(temp)

while fileName != 'end':
    findFiles(os.path.abspath('.'))
    print('\n')
    fileName = input()
    print('input end to exit...\n')