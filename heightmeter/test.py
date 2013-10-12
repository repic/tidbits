#!/usr/bin/env python

import sys, pprint
from xml.dom import minidom

doc = minidom.parse(sys.argv[1])  # parseString also exists
path_strings = [path.getAttribute('x1') for path in doc.getElementsByTagName('line') if 't' in path.getAttribute('id') ]
doc.unlink()

pprint.pprint(path_strings)