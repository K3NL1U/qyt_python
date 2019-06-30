# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


import os

os.mkdir('test')
os.chdir('test')

qytang1 = open('qytang1', 'w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()

qytang2 = open('qytang2', 'w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()

qytang3 = open('qytang3', 'w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()

os.mkdir('qytang4')
os.mkdir('qytang5')

os.chdir('test')
filelist = os.listdir(os.getcwd())

files = []

for i in filelist:
    if os.path.isfile(i):
        for line in open(i):
            if 'qytang' in line:
                files.append(i)

print('文件中包含"qytang"关键字的文件为：')
for i in files:
    print('\t' + i)
