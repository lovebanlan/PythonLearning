import os
import re

def renameFiles(fn, pre, sn, nn):
    flist = os.listdir('.')
    flist.sort()
    for f in flist:
       # print(f)
        ext = os.path.splitext(f)[1];
        if os.path.isdir(f) == False and (ext == fn or ext == '.' + fn):
            fi = os.path.split(f)
            os.rename(fi[0] + fi[1], fi[0] +  getCurName(fn, pre, sn, nn))
            print(fi[0] + fi[1], fi[0], ' =>> ' , getCurName(fn, pre, sn, nn))
            sn += 1

def getCurName(fn, pre, num, nn):
    num = str(num)
    while len(num) < nn:
        num = '0' + num
    return pre + num + fn

print('input extension: ')
fileName = input()
print('input new prefix: ')
prefix = input()
regS = r'^\d{1,5}$';
regE = r'^[1-9]\d{1,4}$';
while True:
    print('input the number you start with: ')
    startNum = input()
    if re.match(regS, startNum):
        break
    else:
        print('format: number from 0 to 99999')

while True:
    print('input the number size: ')
    numberNum = input()
    if re.match(regS, numberNum):
        break
    else:
         print('format: number from 1 to 99999')

startNum = int(startNum)
numberNum = int(numberNum)
if prefix == None:
    prefix = ''
if fileName.find('.') == -1:
    fileName = '.' + fileName;
print('start rename...')
renameFiles(fileName, prefix, startNum, numberNum)
print('rename over...')
print('press any key to exit...')
input()