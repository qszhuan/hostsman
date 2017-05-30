import sys

is_windows = sys.platform == 'win32' or sys.platform == 'cygwin'
is_linux = 'linux' in sys.platform
is_mac = sys.platform == 'darwin'


class Platform(object):
    def is_windows(self):
        return sys.platform == 'win32' or sys.platform == 'cygwin'
    def is_linux(self):
        return 'linux' in sys.platform
    def is_mac(self):
        return sys.platform == 'darwin'