# -*- coding: utf-8 -*-

import sys
from pygments import highlight
from pygments.lexers import *
from pygments.formatters import *
import argparse
from shutil import copyfile
import datetime


class Host:
    def __init__(self):
        platform = sys.platform

        if 'linux' in platform or platform == 'darwin':
            self.hostFile = "/etc/hosts"
        elif platform == 'win32' or platform == 'cygwin':
            self.hostFile = 'c:\windows\system32\drivers\etc\hosts'
        else:
            self.hostFile = '/etc/hosts'

    def list(self):
        with open(self.hostFile, 'r') as f:
            return [line.strip() for line in f]

    def add(self, hostname, ip='127.0.0.1'):
        if self.exists(hostname):
            return False

        with open(self.hostFile, 'a') as f:
            f.write(ip + '\t' + hostname + '\n')
            return True

    def remove(self, hostname):
        if not self.exists(hostname):
            return False,

        now = datetime.datetime.utcnow()
        back_file = self.hostFile + now.strftime("-%Y.%m.%d.%H.%M.%S.%f")
        copyfile(self.hostFile, back_file)
        found = False
        with open(back_file, 'r') as input:
            with open(self.hostFile, 'w') as output:
                for line in input:
                    if line.startswith('#') or line == '\n':
                        output.write(line)
                    elif len(line.split()) == 2 and line.split()[1] == hostname:  # only consider 1 hostname per line
                        found = True
                        continue
                    else:
                        output.write(line)
        return found, back_file

    def exists(self, hostname):
        with open(self.hostFile, 'r') as f:
            for line in list(f):
                if line.startswith('#') or line == '\n':
                    continue
                if line.split()[1] == hostname:
                    return True
            else:
                return False

    def check(self, *host_names):
        result = []
        with open(self.hostFile, 'r') as f:
            for line in list(f):
                if line.startswith('#') or line == '\n':
                    continue
                if line.split()[1] in host_names:
                    result.append(line.strip())

            return result

    def location(self):
        return self.hostFile


def init_parser(file_path):
    parser = argparse.ArgumentParser(description='add, remove or list mappings in hosts file',
                                     epilog='hosts file location: ' + file_path)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l", "--list", action="store_true", help="Show the content of hosts file")
    group.add_argument("-c", "--check", metavar='HOSTNAME', nargs='+',
                       help="Check if the host name existed in the host file")
    group.add_argument("-i", "--insert", metavar='HOSTNAME[:IP]', nargs='+',
                       help="Insert HOSTNAME[:IP] mappings")
    group.add_argument("-r", "--remove", metavar='HOSTNAME', nargs='+',
                       help="Remove mapping for HOSTNAME from hosts file.")
    return parser


def highlight_line(content):
    return highlight(content, PythonLexer(ensurenl=False), TerminalTrueColorFormatter())


def print_highlight(*a_list):
    for each in a_list:
        print(highlight_line(each))


def main():
    host = Host()
    parser = init_parser(host.location())
    args = parser.parse_args()

    if args.list:
        content = host.list()
        print_highlight(*content)
    elif args.check:
        print_highlight('# Search result:')
        result = host.check(*args.check)
        print_highlight(*result)
    elif args.insert:
        print_highlight('# Insert mapping:')
        for each in args.insert:
            arg = each.split(':')
            if host.add(*arg):
                print_highlight('> inserted ' + each)
            else:
                print_highlight('> failed to insert ' + each)
    elif args.remove:
        print_highlight('# Remove mapping:')
        for each in args.remove:
            result = host.remove(each)
            if result[0]:
                print_highlight('## removed ' + each + ', backup file: ' + result[1])
            else:
                print_highlight('## Not found ' + each)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
