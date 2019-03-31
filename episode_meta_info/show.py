#!/usr/bin/env python
from __future__ import print_function
import json
import sys

s = json.loads(open(sys.argv[1]).read())
for x in s:
    print(x + ':', s[x])
