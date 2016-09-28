# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from host import Host
import sys


class TestHost(unittest.TestCase):

    @patch("sys.platform", "linux")
    def test_get_correct_host_file_for_linux(self):
        host = Host()
        self.assertEquals('/etc/hosts', host.hostFile)


    @patch("sys.platform", "win32")
    def test_get_correct_host_file_for_windows(self):
        host = Host()

        self.assertEquals('c:\windows\system32\drivers\etc\hosts', host.hostFile)

    @patch("sys.platform", "darwin")
    def test_get_correct_host_file_for_osx(self):
        host = Host()
        self.assertEquals('/etc/hosts', host.hostFile)

    def test_get_list(self):
        host = Host()
        host.hostFile = './data/hosts'
        host_list = host.list()
        self.assertEquals(len(host_list), 2)
        self.assertEquals("127.0.0.1   my.test1", host_list[0])
        self.assertEquals("127.0.0.2   my.test2", host_list[1])

    def test_if_host_existed(self):
        host = Host()
        host.hostFile = './data/hosts'
        existed = host.exists('my.test1')
        self.assertTrue(existed)

    def test_host_not_existed(self):
        host = Host()
        host.hostFile = './data/hosts'
        existed = host.exists('piupiu')
        self.assertFalse(existed)

    def test_check_host(self):
        host = Host()
        host.hostFile = './data/hosts'
        result = host.check('my.test1')
        self.assertEquals(1, len(result))
        self.assertEquals('127.0.0.1   my.test1', result[0])

    def test_check_non_host(self):
        host = Host()
        host.hostFile = './data/hosts'
        result = host.check('aeiou')
        self.assertEquals(0, len(result))
        # self.assertIsNone(result)

    def test_check_multi_hosts(self):
        host = Host()
        host.hostFile = './data/hosts'
        result = host.check('my.test1', 'my.test2')
        self.assertEquals(2, len(result))
        self.assertEquals('127.0.0.1   my.test1', result[0])
        self.assertEquals('127.0.0.2   my.test2', result[1])

if __name__ == '__main__':
    unittest.main()
