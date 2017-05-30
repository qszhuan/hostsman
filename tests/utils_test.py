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

from utils import *

class TestHost(unittest.TestCase):
    @patch("sys.platform", "linux")
    def test_platform_for_linux(self):
        platform = Platform()
        self.assertFalse(platform.is_windows())
        self.assertTrue(platform.is_linux())
        self.assertFalse(platform.is_mac())
