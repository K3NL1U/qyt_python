# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


def five():
    global num
    num += 1


def main():
    global num
    num = 1
    five()
    print(num)


num = 0
main()
