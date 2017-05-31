# -*- coding: utf-8 -*-

import sys
from pygments import highlight
from pygments.lexers import *
from pygments.formatters import *
import argparse
from shutil import copyfile
import datetime
from HostsLexer import *
from utils import *
from context import *

env = Environment()

class Host:
    def __init__(self):
        platform = Platform()
        if platform.is_linux() or platform.is_mac():
            self.hostFile = "/etc/hosts"
        elif platform.is_windows():
            self.hostFile = 'c:\windows\system32\drivers\etc\hosts'
        else:
            self.hostFile = '/etc/hosts'

    def list(self):
        with open(self.hostFile, 'r') as f:
            return [line.strip() for line in f]

    def add(self, hostname, ip='127.0.0.1'):
        if self.exists(hostname, ip):
            return False

        added = False
        now = datetime.datetime.utcnow()
        back_file = self.hostFile + now.strftime("-%Y.%m.%d.%H.%M.%S.%f")
        copyfile(self.hostFile, back_file)

        with open(back_file, 'r') as input:
            with open(self.hostFile, 'w') as output:
                for line in input:
                    if line.startswith('#') or line == '\n':
                        output.write(line)
                    else:
                        segment = line.split()
                        if ip == segment[0]:
                            segment.append(hostname)
                            added = True
                        output.write(segment[0])
                        output.write('\t')
                        output.write(' '.join(segment[1:]))
                        output.write('\n')
                if not added:
                    output.write(ip)
                    output.write('\t')
                    output.write(hostname)
                    output.write('\n')

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
                    segment = line.split()

                    if line.startswith('#') or line == '\n':
                        output.write(line)
                    elif len(segment) == 2 and hostname == segment[1]:
                        found = True
                        continue
                    elif len(segment) >= 2 and hostname in segment[1:]:
                        found = True
                        segment.remove(hostname)
                        output.write(segment[0])
                        output.write('\t')
                        output.write(' '.join(segment[1:]))
                        output.write('\n')
                    else:
                        output.write(line)
        return found, back_file

    def exists(self, hostname, ip = None):
        with open(self.hostFile, 'r') as f:
            for line in list(f):
                segment = line.split()
                if line.startswith('#') or line == '\n':
                    continue
                if hostname in segment[1:] and (ip is None or ip == segment[0]):
                    return True
            else:
                return False

    def check(self, *host_names):
        result = []
        with open(self.hostFile, 'r') as f:
            for line in list(f):
                if line.startswith('#') or line == '\n':
                    continue
                if len([x for x in line.split()[1:] if x in host_names]):
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
    return highlight(content, HostsLexer(ensurenl=False), TerminalFormatter())


def print_highlight(*a_list):
    for each in a_list:
        env.stdout.write(highlight_line(each) + '\n')
    env.stdout.flush()

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
