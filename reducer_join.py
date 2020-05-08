#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys
from itertools import groupby

current_empid = None
current_data = None

for line in sys.stdin:
    eid,data = line.rstrip().split("\t",1)
    eid = eid.strip()
    data = data.strip()

    if current_empid == eid:
        current_data = current_data+";"+data if data[0] == "$" else data+";"+current_data
    else:
        if current_empid: print(current_empid,";",current_data)
        current_data = data
        current_empid = eid

