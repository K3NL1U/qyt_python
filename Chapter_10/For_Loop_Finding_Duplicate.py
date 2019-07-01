# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


list1 = ['aaa', 111, (4,5), 2.01]
list2 = ['bbb', 333, 111, 3.147, (4,5)]

for i in list1:
    if i in list2:
        print(i, 'is in List1 and List2')
    else:
        print(i, 'only in List1')
