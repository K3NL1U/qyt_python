# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


from SSH_Function import ssh


if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = 'usage: python3 SSH_Function.py -i ipaddr -u username -p password -c command'

    parser = ArgumentParser(usage=usage)

    parser.add_argument('-i', '--ipaddr', dest='ipaddr', help='SSH Server', default='10.0.0.34', type=str)
    parser.add_argument('-u', '--username', dest='username', help='SSH Username', default='ken', type=str)
    parser.add_argument('-p', '--password', dest='password', help='SSH Password', default='Cisc0123', type=str)
    parser.add_argument('-c', '--command', dest='command', help='Shell Command', default='ls', type=str)

    args = parser.parse_args()

    # print(ssh(args.ipaddr, args.username, args.password, cmd=args.command))
