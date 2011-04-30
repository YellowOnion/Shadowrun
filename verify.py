#!/usr/bin/env python2

import fnmatch
import os
import yaml
try:
    from yaml import Cloader as Loader
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

document = ''
for directory in ('metatypes', 'qualities'):
    for root, dirnames, filenames in os.walk(os.path.join(os.path.dirname(__file__), directory)):
        for filename in fnmatch.filter(filenames, '*.yml'):
            full_filename = os.path.join(root, filename)
            print full_filename
            document += open(full_filename).read() + '\n'

SHADOWRUN = yaml.load(document, Loader=Loader)
