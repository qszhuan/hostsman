# -*- coding: utf-8 -*-

from pygments.lexer import RegexLexer
from pygments.token import *

class HostsLexer(RegexLexer):
    name = 'Lexer for hosts file'
    aliases = ['hosts']
    filenames = ['hosts']

    tokens = {
        'root': [
            (r'#.*?$', Name.Decorator),
            (r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', Name.Class),
            (r'.+', Name.Attribute)
        ]
    }