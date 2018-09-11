# -*- coding: utf-8 -*-

import unittest
import sys
from hostsman import Host
import os
import uuid

version_info = sys.version_info
if version_info[0] >= 3 and version_info[1] >= 3: # python2.6 can not use version_info.major
    from unittest.mock import patch
else:
    from mock import patch

dir_path = os.path.dirname(os.path.realpath(__file__))
host_path = os.path.join(dir_path, 'data', 'hosts')

from shutil import copyfile

class TestHost(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHost, self).__init__(*args, **kwargs)
        self.postfix = uuid.uuid4()
        

    def setUp(self):
        self.hostfile = host_path + "-" + str(uuid.uuid4())
        copyfile(host_path, self.hostfile)
        self.host = Host(keepingHistory=False)
        self.host.hostFile = self.hostfile

    def tearDown(self):
        os.remove(self.hostfile)
        pass

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
        host_list = self.host.list()
        self.assertEquals(len(host_list), 3)
        self.assertEquals("127.0.0.1\tmy.test1", host_list[0])
        self.assertEquals("127.0.0.2\tmy.test2 my.test3 my.test1", host_list[1])
        self.assertEquals("127.0.0.3\tmy.test4", host_list[2])

    def test_if_host_existed(self):
        existed = self.host.exists('my.test1')
        self.assertTrue(existed)
        self.assertTrue(self.host.exists("my.test2"))
        self.assertTrue(self.host.exists("my.test3"))

        self.assertTrue(self.host.exists("my.test1", "127.0.0.1"))
        self.assertTrue(self.host.exists("my.test1", "127.0.0.2"))
        self.assertFalse(self.host.exists("my.test1", "127.0.0.3"))

    def test_host_not_existed(self):
        existed = self.host.exists('piupiu')
        self.assertFalse(existed)

    def test_check_host(self):
        result = self.host.check('my.test1')
        self.assertEquals(2, len(result))
        self.assertEquals('127.0.0.1\tmy.test1', result[0])
        self.assertEquals('127.0.0.2\tmy.test2 my.test3 my.test1', result[1])

    def test_check_non_host(self):
        result = self.host.check('aeiou')
        self.assertEquals(0, len(result))
        # self.assertIsNone(result)

    def test_check_multi_hosts(self):
        result = self.host.check('my.test1', 'my.test2')
        self.assertEquals(2, len(result))
        self.assertEquals('127.0.0.1\tmy.test1', result[0])
        self.assertEquals('127.0.0.2\tmy.test2 my.test3 my.test1', result[1])
    
    def test_add_host(self):
        success = self.host.add("add.test.com", "127.0.0.4")
        self.assertTrue(success)
        filelines = len(open(self.hostfile).readlines())
        self.assertEquals(4, filelines)
        result = self.host.check("add.test.com")
        self.assertEquals("127.0.0.4\tadd.test.com", result[0])
    
    def test_add_host_to_existing_ip(self):
        success = self.host.add("add.test.com")
        self.assertTrue(success)
        filelines = len(open(self.hostfile).readlines())
        self.assertEquals(3, filelines)
        result = self.host.check("add.test.com")
        self.assertEquals("127.0.0.1\tmy.test1 add.test.com", result[0])

    def test_remove_non_existing_host(self):
        hostname = "add.test.com"
        success,_ = self.host.remove(hostname)
        self.assertFalse(success)
        self.assertFalse(self.host.exists(hostname))
    
    def test_remove_host(self):
        hostname = "my.test1"
        success,_ = self.host.remove(hostname)
        self.assertTrue(success)
        self.assertFalse(self.host.exists(hostname))



if __name__ == '__main__':
    unittest.main()
