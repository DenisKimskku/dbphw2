#!/usr/bin/env python3

import sys

for line in sys.stdin:
    ########## EDIT HERE ##########
    #mapper for reducer.py
    line = line.strip().split()
    print("{0} {1} {2} {3} {4}".format(line[0], line[1], line[2], line[3], line[4]))

    ########## EDIT HERE ##########