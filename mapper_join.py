#!/usr/bin/env python3
"""mapper.py"""

import sys
import pandas as pd
import codecs
import numpy as np
from sklearn.neighbors import NearestNeighbors

for line in sys.stdin:
	line = line.replace("\n","").replace("\r","").replace("\"","").split(';')
	if line[0] == "Employee ID": continue
	if(len(line[1:]) > 2): print(line[0],"\t", ';'.join(line[1:]))
	else: print(line[0],"\t", *line[1:])



			