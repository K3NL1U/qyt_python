# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


def arg_parse(host, filename, interface):
    print(host)
    print(filename)
    print(interface)


if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = 'usage: python3 Arg_parse.py ipaddress -f filename -i interface'

    parser = ArgumentParser(usage=usage)

    parser.add_argument('-f', '--file', dest='filename', help='Write content to FILE', default='1.txt', type=str)
    parser.add_argument('-i', '--iface', dest='interface', help='Specify an interface', default=1, type=int)
    parser.add_argument(nargs='?', dest='host', help='Specify an host', default='10.1.1.1', type=str)
    args = parser.parse_args()

    arg_parse(args.host, args.filename, args.interface)
