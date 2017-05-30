# -*- coding: utf-8 -*-

import unittest
import sys
from hostsman import Host
import os

version_info = sys.version_info
if version_info[0] >= 3 and version_info[1] >= 3: # python2.6 can not use version_info.major
    from unittest.mock import patch
else:
    from mock import patch

dir_path = os.path.dirname(os.path.realpath(__file__))
host_path = os.path.join(dir_path, 'data', 'hosts')


class TestHost(unittest.TestCase):
    @patch('sys.platform', 'linux')
    def test_get_correct_host_file_for_linux(self):
        host = Host()
        self.assertEquals('/etc/hosts', host.hostFile)

    @patch('sys.platform', 'win32')
    def test_get_correct_host_file_for_windows(self):
        host = Host()
        self.assertEquals('c:\windows\system32\drivers\etc\hosts', host.hostFile)

    @patch('sys.platform', 'darwin')
    def test_get_correct_host_file_for_osx(self):
        host = Host()
        self.assertEquals('/etc/hosts', host.hostFile)

    def test_get_list(self):
        host = Host()
        host.hostFile = host_path
        host_list = host.list()
        self.assertEquals(len(host_list), 3)
        self.assertEquals("127.0.0.1   my.test1", host_list[0])
        self.assertEquals("127.0.0.2   my.test2 my.test3 my.test1", host_list[1])
        self.assertEquals("127.0.0.3   my.test4", host_list[2])

    def test_if_host_existed(self):
        host = Host()
        host.hostFile = host_path
        existed = host.exists('my.test1')
        self.assertTrue(existed)
        self.assertTrue(host.exists("my.test2"))
        self.assertTrue(host.exists("my.test3"))
       
    def test_host_not_existed(self):
        host = Host()
        host.hostFile = host_path
        existed = host.exists('piupiu')
        self.assertFalse(existed)

    def test_check_host(self):
        host = Host()
        host.hostFile = host_path
        result = host.check('my.test1')
        self.assertEquals(2, len(result))
        self.assertEquals('127.0.0.1   my.test1', result[0])
        self.assertEquals('127.0.0.2   my.test2 my.test3 my.test1', result[1])

    def test_check_non_host(self):
        host = Host()
        host.hostFile = host_path
        result = host.check('aeiou')
        self.assertEquals(0, len(result))
        # self.assertIsNone(result)

    def test_check_multi_hosts(self):
        host = Host()
        host.hostFile = host_path
        result = host.check('my.test1', 'my.test2')
        self.assertEquals(2, len(result))
        self.assertEquals('127.0.0.1   my.test1', result[0])
        self.assertEquals('127.0.0.2   my.test2 my.test3 my.test1', result[1])
    


if __name__ == '__main__':
    unittest.main()
