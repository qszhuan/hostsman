import sys

platform = sys.platform

is_windows = platform == 'win32' or platform == 'cygwin'
is_linux = 'linux' in platform
is_mac = platform == 'darwin'